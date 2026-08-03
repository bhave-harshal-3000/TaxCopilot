import os
import json
from dotenv import load_dotenv
from groq import Groq
from app.models.validation_result import ValidationResult

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


class ValidatorAgent:

    @staticmethod
    def python_validate(case_name: str, parsed_documents: list):

        issues = []

        # No documents uploaded
        if len(parsed_documents) == 0:
            issues.append("No documents uploaded.")

        names = set()
        pans = set()
        financial_years = set()

        for document in parsed_documents:
            data = document.model_dump()
            required_fields = getattr(document, "REQUIRED_FIELDS", [])

            # Check only explicitly required fields
            for key in required_fields:
                if data.get(key) is None:
                    readable_key = key.replace("_", " ").title()
                    issues.append(
                        f"{document.document_type}: '{readable_key}' is missing."
                    )

            # Collect values for comparison with robust cross-document check support
            name_keys = [
                "employee_name", "taxpayer_name", "account_holder_name", 
                "borrower_name", "client_name", "donor_name", "winner_name", 
                "professional_name", "partner_name", "freelancer_name", 
                "parent_name", "policyholder_name", "investor_name", 
                "pensioner_name", "business_owner_name", "shareholder_name",
                "member_name", "tenant_name", "deductee_name"
            ]
            for n_key in name_keys:
                if data.get(n_key):
                    names.add(data[n_key])
                    break

            pan_keys = [
                "pan", "employee_pan", "deductee_pan", "donor_pan", 
                "partner_pan", "client_pan"
            ]
            for p_key in pan_keys:
                if data.get(p_key):
                    pans.add(data[p_key])
                    break

            if data.get("financial_year"):
                financial_years.add(data["financial_year"])

            # Invalid values checks
            salary_val = data.get("salary") or data.get("gross_salary") or data.get("basic_salary")
            tds_val = data.get("tds") or data.get("tds_deducted") or data.get("total_tds_deposited")

            if salary_val is not None and salary_val < 0:
                issues.append(f"{document.document_type}: Salary amount cannot be negative.")

            if tds_val is not None and tds_val < 0:
                issues.append(f"{document.document_type}: TDS amount cannot be negative.")

            if salary_val is not None and tds_val is not None and tds_val > salary_val:
                issues.append(f"{document.document_type}: TDS amount cannot be greater than Salary.")

        # Cross-document checks
        if len(names) > 1:
            issues.append(f"Employee name differs across documents: {', '.join(sorted(names))}.")

        if len(pans) > 1:
            issues.append(f"PAN differs across documents: {', '.join(sorted(pans))}.")

        if len(financial_years) > 1:
            issues.append(f"Financial Year differs across documents: {', '.join(sorted(financial_years))}.")

        return ValidationResult(
            valid=len(issues) == 0,
            issues=issues
        )


    
    #LLM VALIDATOR AGENT
    
    @staticmethod
    def llm_review(case_name: str, parsed_documents: list, python_validation: ValidationResult):
        schema = ValidationResult.model_json_schema()
        
        documents_json = json.dumps([doc.model_dump() for doc in parsed_documents], indent=2)

        validation_json = json.dumps(python_validation.model_dump(), indent=2)
        
        system_prompt = f"""
            You are a Senior Deloitte Tax Consultant reviewing an Indian income tax filing case.

            You will receive:
            - Client case details
            - Parsed tax documents
            - Findings from the Python Validator

            Your role is NOT to repeat the Python Validator.

            Your responsibilities are:

            1. Review the overall case from a tax consultant's perspective.
            2. Explain the implications of issues already found by the Python Validator.
            3. Identify reasoning-based issues that cannot be detected using simple rule-based validation.
            4. Suggest genuinely missing supporting documents only when necessary.
            5. Determine whether the case appears ready for tax computation.

            Do NOT:
            - Repeat Python Validator findings.
            - Perform deterministic validations already handled by Python.
            - Calculate taxes.
            - Make legal decisions.
            - Tell the user to restart.
            - Assume valid tax scenarios are suspicious.

            Examples of VALID scenarios:
            - Negative STCG/LTCG (capital loss)
            - Zero TDS
            - Multiple employers
            - Multiple broker statements
            - Multiple bank accounts

            If uncertain, recommend manual review instead of making assumptions.

            Return ONLY valid JSON matching this schema.

            Schema:
            {schema}
        """
            
        user_prompt = f"""
            Case Name:
            {case_name}

            Parsed Documents:
            {documents_json}

            Python Validation:
            {validation_json}
        """
        
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            temperature=0,
            response_format={"type": "json_object"},
            messages=[
                {
                    "role": "system",
                    "content": system_prompt
                },
                {
                    "role": "user",
                    "content": user_prompt
                }
            ]
        )

        return ValidationResult.model_validate_json(
            response.choices[0].message.content
        )                        




