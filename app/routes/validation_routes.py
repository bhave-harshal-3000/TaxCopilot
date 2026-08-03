from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.models.case import TaxCase
from app.models.parsed_document import ParsedDocument
from app.models.document_registry import DOCUMENT_SCHEMAS
from app.agents.validator_agent import ValidatorAgent

router = APIRouter()

@router.post("/cases/{case_id}/validate")
def validate_case(case_id: int, db: Session = Depends(get_db)):
    tax_case = (
        db.query(TaxCase)
        .filter(TaxCase.id == case_id)
        .first()
    )

    if not tax_case:
        return {
            "error": "Case not found."
        }
    
    documents = (
        db.query(ParsedDocument)
        .filter(ParsedDocument.case_id == case_id)
        .all()
    )
    
    parsed_documents = []

    for document in documents:
        schema = DOCUMENT_SCHEMAS.get(document.document_type)

        if not schema:
            continue

        parsed = schema.model_validate(document.parsed_json)
        parsed_documents.append(parsed)
    
    python_result = ValidatorAgent.python_validate(
        tax_case.client_name,
        parsed_documents
    )
    
    llm_result = ValidatorAgent.llm_review(
        tax_case.client_name,
        parsed_documents,
        python_result
    )
    
    return {
        "python_validation": python_result.model_dump(),
        "llm_review": llm_result.model_dump()
    }