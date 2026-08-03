"""
AI Tax Copilot — Streamlit Frontend
=====================================
Single-file frontend that talks to the FastAPI backend running at
http://127.0.0.1:8000.

Endpoints used:
  POST /cases                          → create_case()
  POST /cases/{case_id}/documents      → upload_document()
  POST /cases/{case_id}/validate       → validate_case()  (TODO if missing)

Session state keys (frontend only stores case metadata — backend is source of truth):
  case_id          : int   — ID returned by POST /cases
  client_name      : str
  financial_year   : str
  case_created     : bool
  doc_results      : dict[str, dict]  — keyed by document_type; value is parsed response
                     TODO: replace with GET /cases/{case_id}/documents once available
  validation_result: dict | None      — last result from POST /cases/{case_id}/validate
"""

import time
from collections import OrderedDict
from typing import Optional

import requests
import streamlit as st

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

BASE_URL = "http://127.0.0.1:8000"
FINANCIAL_YEARS = ["2025-26", "2026-27"]

DOCUMENT_TYPES = [
    "Form16",
    "AIS",
    "Broker Statement",
    "Bank Statement",
    "Form26AS",
]

REQUEST_TIMEOUT = 60  # seconds — AI parsing can be slow

# ---------------------------------------------------------------------------
# Page config (must be the very first Streamlit call)
# ---------------------------------------------------------------------------

st.set_page_config(
    page_title="AI Tax Copilot",
    page_icon="🧾",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ---------------------------------------------------------------------------
# Session-state initialisation
# ---------------------------------------------------------------------------

def init_session_state() -> None:
    """Initialise all session-state keys on first run.

    The frontend intentionally stores ONLY case metadata here.
    Parsed document data lives in doc_results (keyed by document_type so that
    re-uploading the same doc type replaces the old entry — no duplicates).
    The backend database remains the authoritative source of truth.
    """
    defaults: dict = {
        "case_id": None,
        "client_name": "",
        "financial_year": FINANCIAL_YEARS[0],
        "case_created": False,
        # dict[document_type -> {"filename": str, "parsed": dict}]
        # TODO: replace with GET /cases/{case_id}/documents once that endpoint exists
        "doc_results": OrderedDict(),
        "validation_result": None,
        "calculation_result": None,
        "backend_alive": False,
    }
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value


init_session_state()

# ---------------------------------------------------------------------------
# API helper functions
# ---------------------------------------------------------------------------

def is_backend_alive() -> bool:
    """Quick ping to check whether the backend is reachable."""
    try:
        requests.get(BASE_URL, timeout=5)
        return True  # any HTTP response means server is up
    except requests.exceptions.ConnectionError:
        return False
    except Exception:
        return False


def format_validation_issues(issues: list) -> list[str]:
    """Convert a list of validation issue dicts or strings into readable bullet strings."""
    bullets: list[str] = []
    for item in issues:
        if isinstance(item, dict):
            # Support both {"message": ...} and {"field": ..., "error": ...} shapes
            msg = (
                item.get("message")
                or item.get("error")
                or item.get("description")
                or str(item)
            )
            bullets.append(str(msg))
        else:
            bullets.append(str(item))
    return bullets


def create_case(client_name: str, financial_year: str) -> Optional[dict]:
    """
    POST /cases
    Returns the created case dict on success, None on failure.
    """
    payload = {
        "client_name": client_name,
        "financial_year": financial_year,
    }
    try:
        resp = requests.post(
            f"{BASE_URL}/cases",
            json=payload,
            timeout=REQUEST_TIMEOUT,
        )
        resp.raise_for_status()
        return resp.json()
    except requests.exceptions.ConnectionError:
        st.error("❌ Backend not running. Please start the FastAPI server and refresh.")
        return None
    except requests.exceptions.HTTPError as exc:
        st.error(
            f"❌ Failed to create case — HTTP {exc.response.status_code}: "
            f"{exc.response.text}"
        )
        return None
    except Exception as exc:
        st.error(f"❌ Unexpected error while creating case: {exc}")
        return None


def upload_document(case_id: int, file, document_type: str) -> Optional[dict]:
    """
    POST /cases/{case_id}/documents  (multipart/form-data)
    Sends both the PDF file and document_type as a form field.
    Returns the parsed document dict on success, None on failure.
    """
    try:
        files = {"file": (file.name, file.getvalue(), "application/pdf")}
        data = {"document_type": document_type}
        resp = requests.post(
            f"{BASE_URL}/cases/{case_id}/documents",
            files=files,
            data=data,
            timeout=REQUEST_TIMEOUT,
        )
        resp.raise_for_status()
        return resp.json()
    except requests.exceptions.ConnectionError:
        st.error("❌ Backend not running. Please start the FastAPI server.")
        return None
    except requests.exceptions.HTTPError as exc:
        st.error(
            f"❌ Upload failed for **{file.name}** — "
            f"HTTP {exc.response.status_code}: {exc.response.text}"
        )
        return None
    except Exception as exc:
        st.error(f"❌ Unexpected error uploading **{file.name}**: {exc}")
        return None


def validate_case(case_id: int) -> Optional[dict]:
    """
    POST /cases/{case_id}/validate
    TODO: Implement this endpoint in the backend.
    Returns the validation result dict on success, None on failure.
    """
    try:
        resp = requests.post(
            f"{BASE_URL}/cases/{case_id}/validate",
            timeout=REQUEST_TIMEOUT,
        )
        resp.raise_for_status()
        return resp.json()
    except requests.exceptions.ConnectionError:
        return None  # caller handles gracefully
    except requests.exceptions.HTTPError as exc:
        if exc.response.status_code == 404:
            return None  # endpoint not yet implemented — caller shows TODO message
        st.error(
            f"❌ Validation error — HTTP {exc.response.status_code}: "
            f"{exc.response.text}"
        )
        return None
    except Exception as exc:
        st.error(f"❌ Unexpected error during validation: {exc}")
        return None


def calculate_tax(case_id: int) -> Optional[dict]:
    """
    POST /cases/{case_id}/calculate
    Returns the calculation result dict on success, None on failure.
    """
    try:
        resp = requests.post(
            f"{BASE_URL}/cases/{case_id}/calculate",
            timeout=120,
        )
        resp.raise_for_status()
        return resp.json()
    except requests.exceptions.ConnectionError:
        st.error("❌ Backend not running. Please start the FastAPI server.")
        return None
    except requests.exceptions.HTTPError as exc:
        st.error(
            f"❌ Calculation failed — HTTP {exc.response.status_code}: "
            f"{exc.response.text}"
        )
        return None
    except Exception as exc:
        st.error(f"❌ Unexpected error during calculation: {exc}")
        return None


# ---------------------------------------------------------------------------
# Sidebar
# ---------------------------------------------------------------------------

def render_sidebar(backend_alive: bool) -> None:
    """Render the persistent sidebar with current case info and backend status."""
    with st.sidebar:
        st.markdown("## 🧾 AI Tax Copilot")
        st.markdown("---")

        # ── Backend status ──────────────────────────────────────────────────
        if backend_alive:
            st.success("🟢 Backend Connected")
        else:
            st.error("🔴 Backend Offline")

        st.markdown("---")
        st.markdown("### 📁 Current Case")

        if st.session_state.case_created:
            st.markdown(f"**Case ID:** `{st.session_state.case_id}`")
            st.markdown(f"**Client:** {st.session_state.client_name}")
            st.markdown(f"**Financial Year:** {st.session_state.financial_year}")
            doc_count = len(st.session_state.doc_results)
            st.markdown(f"**Documents Uploaded:** {doc_count}")

            if doc_count > 0:
                st.markdown("---")
                st.markdown("### 📄 Documents")
                for doc_type, doc in st.session_state.doc_results.items():
                    status_icon = "✅" if doc["parsed"] else "❌"
                    st.markdown(f"{status_icon} {doc_type}")
                    st.caption(f"   {doc['filename']}")
        else:
            st.info("No active case. Create a case to get started.")

        st.markdown("---")
        st.caption("Powered by FastAPI + Streamlit")

        # Reset button — useful during development / testing
        if st.session_state.case_created:
            st.markdown("---")
            if st.button("🔄 Start New Session", use_container_width=True):
                for key in list(st.session_state.keys()):
                    del st.session_state[key]
                st.rerun()


# ---------------------------------------------------------------------------
# Section 1 — Create Tax Case
# ---------------------------------------------------------------------------

def render_create_case_section() -> None:
    """Render the 'Create Tax Case' form at the top of the page."""
    st.markdown("## Step 1 — Create Tax Case")

    with st.container(border=True):
        col1, col2, col3 = st.columns([3, 2, 1], vertical_alignment="bottom")

        with col1:
            client_name = st.text_input(
                "👤 Client Name",
                placeholder="e.g. Rahul Sharma",
                key="input_client_name",
                disabled=st.session_state.case_created,
            )

        with col2:
            financial_year = st.selectbox(
                "📅 Financial Year",
                options=FINANCIAL_YEARS,
                key="input_financial_year",
                disabled=st.session_state.case_created,
            )

        with col3:
            create_clicked = st.button(
                "🚀 Create Case",
                use_container_width=True,
                type="primary",
                disabled=st.session_state.case_created,
            )

        if create_clicked:
            if not client_name.strip():
                st.warning("⚠️ Please enter the client's name before creating a case.")
            else:
                with st.spinner("Creating case…"):
                    result = create_case(client_name.strip(), financial_year)

                if result:
                    # Store only case metadata — backend DB is the source of truth
                    st.session_state.case_id = result["id"]
                    st.session_state.client_name = result["client_name"]
                    st.session_state.financial_year = result["financial_year"]
                    st.session_state.case_created = True
                    # st.rerun() is required here so the sidebar and locked inputs
                    # reflect the new case immediately.
                    st.rerun()

        # Show active case info banner when already created
        if st.session_state.case_created:
            st.success(
                f"✅ Active Case — ID: **{st.session_state.case_id}** | "
                f"Client: **{st.session_state.client_name}** | "
                f"FY: **{st.session_state.financial_year}**"
            )


# ---------------------------------------------------------------------------
# Section 2 — Upload Documents
# ---------------------------------------------------------------------------

def render_upload_section() -> None:
    """Render the document upload section (one document at a time)."""
    st.markdown("## Step 2 — Upload Document")

    if not st.session_state.case_created:
        st.info("ℹ️ Please create a case first before uploading documents.")
        return

    with st.container(border=True):
        col1, col2 = st.columns([2, 3])

        with col1:
            # Document type selector
            document_type = st.selectbox(
                "📂 Document Type",
                options=DOCUMENT_TYPES,
                key="selected_document_type",
                help="Select the type of document you are uploading. You can search by typing.",
            )

        with col2:
            uploaded_file = st.file_uploader(
                "📎 Select a PDF document",
                type=["pdf"],
                accept_multiple_files=False,
                key="file_uploader",
            )

        if uploaded_file:
            st.markdown(f"📄 `{uploaded_file.name}` selected")

        upload_clicked = st.button(
            "⬆️ Upload Document",
            disabled=not uploaded_file,
            type="primary",
        )

        if upload_clicked and uploaded_file:
            with st.spinner(
                f"Uploading & parsing **{uploaded_file.name}** as **{document_type}**…"
            ):
                parsed = upload_document(
                    st.session_state.case_id,
                    uploaded_file,
                    document_type,
                )

            if parsed is not None:
                # Deduplicate by document_type — re-uploading the same type replaces
                # the old entry, matching the backend's upsert behaviour.
                # TODO: once GET /cases/{case_id}/documents is available, fetch from
                #       backend instead of maintaining doc_results in session state.
                st.session_state.doc_results[document_type] = {
                    "filename": uploaded_file.name,
                    "parsed": parsed,
                }
                st.success(
                    f"✅ **{document_type}** uploaded and parsed successfully!"
                )
            else:
                # Failed upload — keep visible so the user sees the error card
                fallback_key = f"error::{uploaded_file.name}"
                st.session_state.doc_results[fallback_key] = {
                    "filename": uploaded_file.name,
                    "parsed": None,
                }
                st.error(
                    f"❌ Upload failed for **{uploaded_file.name}**. "
                    "Check error messages above."
                )

            # Reset validation result so the user must re-run after new uploads
            st.session_state.validation_result = None
            # No st.rerun() here — results render naturally on the same run


# ---------------------------------------------------------------------------
# Section 3 — Parsed Results
# ---------------------------------------------------------------------------

def render_parsed_results_section() -> None:
    """Display parsed JSON results, one card per document_type (no duplicates)."""
    if not st.session_state.doc_results:
        return

    st.markdown("## Step 3 — Parsed Document Results")

    with st.container(border=True):
        for doc_type, doc in st.session_state.doc_results.items():
            filename = doc["filename"]
            parsed = doc["parsed"]

            # Use document_type as the expander label — cleaner than raw filename
            label = f"📄 {doc_type}" if not doc_type.startswith("error::") else f"❌ {filename}"

            with st.expander(label, expanded=False):
                if parsed is None:
                    st.error(
                        f"Parsing failed for **{filename}**. "
                        "No data returned from the backend."
                    )
                else:
                    st.markdown(f"**Filename:** `{filename}`")
                    st.markdown("**Full Parsed Response:**")
                    st.json(parsed)


# ---------------------------------------------------------------------------
# Section 4 — Validation
# ---------------------------------------------------------------------------

def render_validation_issues(issues: list) -> None:
    """Render a list of validation issues as readable bullet points."""
    bullets = format_validation_issues(issues)
    if bullets:
        for bullet in bullets:
            st.markdown(f"• {bullet}")
    else:
        st.success("✅ No issues found")


def render_validation_section() -> None:
    """
    Dedicated 'Validate Case' section.
    Validation is ALWAYS manual — never triggered automatically after uploads.
    Falls back gracefully if the endpoint is not yet implemented.
    """
    if not st.session_state.doc_results:
        return

    st.markdown("## Step 4 — Validate Case")

    with st.container(border=True):
        col1, col2 = st.columns([3, 1], vertical_alignment="bottom")

        with col1:
            st.markdown(
                "Run automated validation to check for inconsistencies and "
                "get an LLM-powered review of the uploaded documents."
            )

        with col2:
            run_validation = st.button(
                "🔍 Validate Case",
                type="primary",
                use_container_width=True,
            )

        if run_validation:
            with st.spinner("Running validation — this may take a moment…"):
                result = validate_case(st.session_state.case_id)
            st.session_state.validation_result = result

            if result is None:
                # TODO: Backend — implement POST /cases/{case_id}/validate
                st.info(
                    "ℹ️ **TODO**: The `/cases/{case_id}/validate` endpoint is not yet "
                    "implemented. Validation results will appear here once available."
                )

        # ── Display results (persisted across rerenders) ─────────────────────
        result = st.session_state.validation_result
        if result is None:
            return

        st.markdown("---")
        st.success("✅ Validation complete!")
        vcol1, vcol2 = st.columns(2)

        # ── Python Validation ────────────────────────────────────────────────
        with vcol1:
            st.markdown("### 🐍 Python Validation")
            py_val = result.get("python_validation")
            if py_val is None:
                st.info("No Python validation data returned.")
            else:
                issues = []
                if isinstance(py_val, dict):
                    status = str(py_val.get("status", "unknown")).lower()
                    issues = py_val.get("issues") or py_val.get("errors") or []
                    if status == "pass" and not issues:
                        st.success("✅ No issues found")
                    elif status == "fail" or issues:
                        st.warning(f"⚠️ Issues Found")
                        render_validation_issues(issues)
                    else:
                        st.warning(f"⚠️ Status: {status}")
                elif isinstance(py_val, list):
                    issues = py_val
                    if issues:
                        st.warning("⚠️ Issues Found")
                        render_validation_issues(issues)
                    else:
                        st.success("✅ No issues found")
                else:
                    st.write(py_val)

        # ── LLM Review ───────────────────────────────────────────────────────
        with vcol2:
            st.markdown("### 🤖 LLM Review")
            llm_review = result.get("llm_review")
            if llm_review is None:
                st.info("No LLM review returned.")
            elif isinstance(llm_review, str):
                # Plain text review — render as markdown (may contain bullets)
                issues_in_review = [
                    line.lstrip("- •*").strip()
                    for line in llm_review.splitlines()
                    if line.strip().startswith(("-", "•", "*"))
                ]
                if issues_in_review:
                    st.warning("⚠️ Issues Found")
                    for item in issues_in_review:
                        st.markdown(f"• {item}")
                else:
                    st.markdown(llm_review)
            elif isinstance(llm_review, list):
                if llm_review:
                    st.warning("⚠️ Issues Found")
                    render_validation_issues(llm_review)
                else:
                    st.success("✅ No issues found")
            elif isinstance(llm_review, dict):
                issues = llm_review.get("issues") or llm_review.get("errors") or []
                if issues:
                    st.warning("⚠️ Issues Found")
                    render_validation_issues(issues)
                else:
                    st.success("✅ No issues found")
                    summary = llm_review.get("summary")
                    if summary:
                        st.markdown(summary)
            else:
                st.write(llm_review)


# ---------------------------------------------------------------------------
# Section 5 — Calculate Tax
# ---------------------------------------------------------------------------

def render_calculation_section() -> None:
    """Render the 'Calculate Tax' section after validation."""
    if not st.session_state.doc_results:
        return

    st.markdown("## Step 5 — Calculate Tax")

    with st.container(border=True):
        col1, col2 = st.columns([3, 1], vertical_alignment="bottom")

        with col1:
            st.markdown(
                "Run the full tax calculation pipeline: build financial profile, "
                "compute taxes, generate AI explanation, and assemble the final report."
            )

        with col2:
            run_calculation = st.button(
                "🧮 Calculate Tax",
                type="primary",
                use_container_width=True,
            )

        if run_calculation:
            with st.spinner("Calculating taxes — this may take a moment…"):
                result = calculate_tax(st.session_state.case_id)
            st.session_state.calculation_result = result

            if result is None:
                st.error(
                    "❌ Tax calculation failed. Check error messages above."
                )

        # ── Display results (persisted across rerenders) ─────────────────────
        calc = st.session_state.calculation_result
        if calc is None:
            return

        st.markdown("---")
        st.success("✅ Tax calculation complete!")

        # ── Financial Profile ────────────────────────────────────────────────
        st.markdown("### 📊 Financial Profile")
        with st.expander("View Financial Profile JSON", expanded=False):
            st.json(calc.get("financial_profile", {}))

        # ── Tax Result ───────────────────────────────────────────────────────
        st.markdown("### 🧾 Tax Result")
        tax_result = calc.get("tax_result", {})

        m1, m2, m3, m4 = st.columns(4)
        with m1:
            st.metric(
                "Gross Total Income",
                f"₹{tax_result.get('gross_total_income', 0):,.2f}"
            )
        with m2:
            st.metric(
                "Taxable Income",
                f"₹{tax_result.get('taxable_income', 0):,.2f}"
            )
        with m3:
            st.metric(
                "Total Tax Liability",
                f"₹{tax_result.get('total_tax_liability', 0):,.2f}"
            )
        with m4:
            refund = tax_result.get("refund", 0)
            payable = tax_result.get("tax_payable", 0)
            if refund > 0:
                st.metric("Refund", f"₹{refund:,.2f}")
            elif payable > 0:
                st.metric("Tax Payable", f"₹{payable:,.2f}")
            else:
                st.metric("Balance", "₹0.00")

        # Additional tax details
        with st.expander("View Detailed Tax Breakdown", expanded=False):
            detail_cols = st.columns(3)
            with detail_cols[0]:
                st.metric("Total Deductions", f"₹{tax_result.get('total_deductions', 0):,.2f}")
                st.metric("Tax Before Rebate", f"₹{tax_result.get('tax_before_rebate', 0):,.2f}")
            with detail_cols[1]:
                st.metric("Rebate", f"₹{tax_result.get('rebate', 0):,.2f}")
                st.metric("Cess (4%)", f"₹{tax_result.get('cess', 0):,.2f}")
            with detail_cols[2]:
                st.metric("TDS", f"₹{tax_result.get('tds', 0):,.2f}")
                st.metric("Advance Tax", f"₹{tax_result.get('advance_tax', 0):,.2f}")

        # ── Final Report ─────────────────────────────────────────────────────
        st.markdown("### 📋 Final Report")
        with st.expander("View Full Report JSON", expanded=False):
            st.json(calc.get("report", {}))


# ---------------------------------------------------------------------------
# Main layout
# ---------------------------------------------------------------------------

def main() -> None:
    # ── Backend health check (once per render cycle) ────────────────────────
    backend_alive = is_backend_alive()
    st.session_state.backend_alive = backend_alive

    if not backend_alive:
        # Still render sidebar so the user sees the 🔴 status indicator
        render_sidebar(backend_alive=False)
        st.error(
            "❌ **Backend not running.**  \n"
            "Please start the FastAPI server with:  \n"
            "`uvicorn app.main:app --reload`  \n"
            "then refresh this page."
        )
        st.stop()

    # ── Sidebar ─────────────────────────────────────────────────────────────
    render_sidebar(backend_alive=True)

    # ── Hero header ─────────────────────────────────────────────────────────
    st.markdown(
        "<h1 style='text-align:center;'>🧾 AI Tax Copilot</h1>",
        unsafe_allow_html=True,
    )
    st.markdown(
        "<p style='text-align:center; color:grey;'>"
        "Intelligent document parsing &amp; tax validation powered by AI</p>",
        unsafe_allow_html=True,
    )
    st.markdown("---")

    # ── Main sections ───────────────────────────────────────────────────────
    render_create_case_section()
    st.markdown("")

    render_upload_section()
    st.markdown("")

    render_parsed_results_section()
    st.markdown("")

    render_validation_section()
    st.markdown("")

    render_calculation_section()


if __name__ == "__main__":
    main()
