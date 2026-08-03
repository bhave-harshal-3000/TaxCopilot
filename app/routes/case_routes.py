from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.models.case import TaxCase

router = APIRouter()


class CreateCaseRequest(BaseModel):
    client_name: str
    financial_year: str


@router.post("/cases")
def create_case(
    request: CreateCaseRequest,
    db: Session = Depends(get_db)
):

    case = TaxCase(
        client_name=request.client_name,
        financial_year=request.financial_year
    )

    db.add(case)
    db.commit()
    db.refresh(case)

    return case