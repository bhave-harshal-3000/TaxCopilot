from typing import ClassVar
from pydantic import BaseModel


class BusinessIncomeStatementData(BaseModel):
    document_type: str
    business_owner_name: str | None = None
    pan: str | None = None
    business_name: str | None = None
    nature_of_business: str | None = None
    financial_year: str | None = None
    gross_receipts: float | None = None
    business_expenses: float | None = None
    net_business_income: float | None = None
    presumptive_taxation_applicable: bool | None = None
    section_44ad_applicable: bool | None = None
    section_44ae_applicable: bool | None = None
    tax_audit_required: bool | None = None
    turnover_threshold_exceeded: bool | None = None
    REQUIRED_FIELDS: ClassVar[list[str]] = ['business_owner_name', 'pan', 'financial_year', 'gross_receipts', 'net_business_income']
