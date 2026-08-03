from typing import ClassVar
from pydantic import BaseModel


class NPSStatementData(BaseModel):
    document_type: str
    subscriber_name: str | None = None
    pran: str | None = None
    pan: str | None = None
    financial_year: str | None = None
    tier1_opening_balance: float | None = None
    tier1_employee_contribution: float | None = None
    tier1_employer_contribution: float | None = None
    tier1_returns: float | None = None
    tier1_closing_balance: float | None = None
    tier2_opening_balance: float | None = None
    tier2_contributions: float | None = None
    tier2_closing_balance: float | None = None
    deduction_80ccd1: float | None = None
    deduction_80ccd1b: float | None = None
    deduction_80ccd2: float | None = None
    REQUIRED_FIELDS: ClassVar[list[str]] = ['subscriber_name', 'pran', 'pan', 'financial_year']
