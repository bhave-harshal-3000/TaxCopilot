from typing import ClassVar
from pydantic import BaseModel


class FDInterestCertificateData(BaseModel):
    document_type: str
    depositor_name: str | None = None
    pan: str | None = None
    bank_name: str | None = None
    fd_account_number: str | None = None
    financial_year: str | None = None
    fd_principal_amount: float | None = None
    interest_rate_percent: float | None = None
    interest_credited: float | None = None
    tds_deducted: float | None = None
    net_interest_paid: float | None = None
    fd_start_date: str | None = None
    fd_maturity_date: str | None = None
    REQUIRED_FIELDS: ClassVar[list[str]] = ['depositor_name', 'pan', 'financial_year', 'interest_credited']
