from typing import ClassVar
from pydantic import BaseModel


class ProfessionalIncomeStatementData(BaseModel):
    document_type: str
    professional_name: str | None = None
    pan: str | None = None
    profession: str | None = None
    financial_year: str | None = None
    gross_professional_receipts: float | None = None
    professional_expenses: float | None = None
    net_professional_income: float | None = None
    presumptive_taxation_applicable: bool | None = None
    section_44ada_applicable: bool | None = None
    tax_audit_required: bool | None = None
    tds_deducted_by_clients: float | None = None
    REQUIRED_FIELDS: ClassVar[list[str]] = ['professional_name', 'pan', 'financial_year', 'gross_professional_receipts', 'net_professional_income']
