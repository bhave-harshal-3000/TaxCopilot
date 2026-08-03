from typing import ClassVar
from pydantic import BaseModel


class Form16AData(BaseModel):
    document_type: str
    deductee_name: str | None = None
    deductee_pan: str | None = None
    deductor_name: str | None = None
    deductor_tan: str | None = None
    financial_year: str | None = None
    quarter: str | None = None
    nature_of_payment: str | None = None
    amount_paid: float | None = None
    tds_deducted: float | None = None
    tds_deposited: float | None = None
    challan_identification_number: str | None = None
    REQUIRED_FIELDS: ClassVar[list[str]] = ['deductee_name', 'deductee_pan', 'financial_year', 'amount_paid', 'tds_deducted']
