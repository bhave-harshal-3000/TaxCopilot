from typing import ClassVar
from pydantic import BaseModel


class PPFPassbookData(BaseModel):
    document_type: str
    account_holder_name: str | None = None
    pan: str | None = None
    ppf_account_number: str | None = None
    bank_or_post_office: str | None = None
    financial_year: str | None = None
    opening_balance: float | None = None
    deposits_during_year: float | None = None
    interest_credited: float | None = None
    closing_balance: float | None = None
    maturity_date: str | None = None
    loan_outstanding: float | None = None
    REQUIRED_FIELDS: ClassVar[list[str]] = ['account_holder_name', 'ppf_account_number', 'financial_year', 'closing_balance']
