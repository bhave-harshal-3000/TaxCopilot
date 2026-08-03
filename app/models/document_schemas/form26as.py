from typing import ClassVar
from pydantic import BaseModel


class Form26ASData(BaseModel):
    document_type: str
    taxpayer_name: str | None = None
    pan: str | None = None
    financial_year: str | None = None
    assessment_year: str | None = None
    total_tds_salary: float | None = None
    total_tds_other_sources: float | None = None
    total_advance_tax: float | None = None
    total_self_assessment_tax: float | None = None
    total_tax_paid: float | None = None
    total_refund: float | None = None
    high_value_transactions_count: int | None = None
    REQUIRED_FIELDS: ClassVar[list[str]] = ['taxpayer_name', 'pan', 'financial_year', 'total_tax_paid']
