from typing import ClassVar
from pydantic import BaseModel


class SavingsInterestCertificateData(BaseModel):
    document_type: str
    account_holder_name: str | None = None
    pan: str | None = None
    bank_name: str | None = None
    account_number: str | None = None
    financial_year: str | None = None
    interest_credited: float | None = None
    tds_deducted: float | None = None
    net_interest_paid: float | None = None
    exempt_under_80tta: float | None = None
    exempt_under_80ttb: float | None = None
    REQUIRED_FIELDS: ClassVar[list[str]] = ['account_holder_name', 'pan', 'financial_year', 'interest_credited']
