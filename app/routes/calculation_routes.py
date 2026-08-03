from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.models.case import TaxCase
from app.models.parsed_document import ParsedDocument
from app.models.document_registry import DOCUMENT_SCHEMAS
from app.services.financial_profile_builder import FinancialProfileBuilder
from app.services.tax_calculator import TaxCalculator
from app.agents.explanation_agent import ExplanationAgent
from app.services.report_generator import ReportGenerator

router = APIRouter()


@router.post("/cases/{case_id}/calculate")
def calculate_tax(case_id: int, db: Session = Depends(get_db)):

    # 1. Lookup the case
    tax_case = (
        db.query(TaxCase)
        .filter(TaxCase.id == case_id)
        .first()
    )

    if not tax_case:
        raise HTTPException(
            status_code=404,
            detail="Case not found."
        )

    # 2. Read all ParsedDocument rows for the case
    documents = (
        db.query(ParsedDocument)
        .filter(ParsedDocument.case_id == case_id)
        .all()
    )

    if not documents:
        raise HTTPException(
            status_code=400,
            detail="No parsed documents found for this case. Upload documents first."
        )

    # 3. Deserialize parsed_json into correct Pydantic schema
    parsed_documents = []

    for document in documents:
        schema = DOCUMENT_SCHEMAS.get(document.document_type)

        if not schema:
            continue

        parsed = schema.model_validate(document.parsed_json)
        parsed_documents.append(parsed)

    # 4. Build FinancialProfile
    profile = FinancialProfileBuilder.build(parsed_documents)

    # 5. Calculate taxes
    result = TaxCalculator.calculate(profile)

    # 6. Generate AI explanation
    explanation = ExplanationAgent.explain(profile, result)

    # 7. Generate structured report
    report = ReportGenerator.generate(profile, result, explanation)

    # 8. Return clean JSON
    return {
        "financial_profile": profile.model_dump(),
        "tax_result": result.model_dump(),
        "explanation": explanation.model_dump(),
        "report": report.model_dump(),
    }
