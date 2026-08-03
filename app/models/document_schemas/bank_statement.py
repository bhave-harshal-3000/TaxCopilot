from typing import ClassVar
from pydantic import BaseModel


class BankStatementData(BaseModel):
    document_type: str
    account_holder_name: str | None = None
    pan: str | None = None
    account_number: str | None = None
    ifsc_code: str | None = None
    bank_name: str | None = None
    branch: str | None = None
    financial_year: str | None = None
    opening_balance: float | None = None
    total_credits: float | None = None
    total_debits: float | None = None
    closing_balance: float | None = None
    interest_credited: float | None = None
    tds_on_interest: float | None = None
    cash_deposits: float | None = None
    cash_withdrawals: float | None = None
    REQUIRED_FIELDS: ClassVar[list[str]] = ['account_holder_name', 'account_number', 'financial_year', 'closing_balance']
