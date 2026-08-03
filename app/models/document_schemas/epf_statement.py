from typing import ClassVar
from pydantic import BaseModel


class EPFStatementData(BaseModel):
    document_type: str
    member_name: str | None = None
    uan: str | None = None
    pan: str | None = None
    employer_name: str | None = None
    financial_year: str | None = None
    opening_balance: float | None = None
    employee_contribution: float | None = None
    employer_contribution: float | None = None
    voluntary_pf_contribution: float | None = None
    interest_credited: float | None = None
    closing_balance: float | None = None
    withdrawal_amount: float | None = None
    taxable_interest: float | None = None
    REQUIRED_FIELDS: ClassVar[list[str]] = ['member_name', 'uan', 'pan', 'financial_year', 'closing_balance']
