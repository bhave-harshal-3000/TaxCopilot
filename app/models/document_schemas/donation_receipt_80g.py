from typing import ClassVar
from pydantic import BaseModel


class DonationReceipt80GData(BaseModel):
    document_type: str
    donor_name: str | None = None
    donor_pan: str | None = None
    trust_or_institution_name: str | None = None
    trust_pan: str | None = None
    trust_80g_registration_number: str | None = None
    trust_address: str | None = None
    financial_year: str | None = None
    donation_amount: float | None = None
    payment_mode: str | None = None
    receipt_number: str | None = None
    eligible_deduction_percentage: float | None = None
    qualifying_limit_applicable: bool | None = None
    deductible_amount: float | None = None
    REQUIRED_FIELDS: ClassVar[list[str]] = ['donor_name', 'donor_pan', 'trust_or_institution_name', 'donation_amount', 'financial_year']
