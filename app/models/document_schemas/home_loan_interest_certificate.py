from typing import ClassVar
from pydantic import BaseModel


class HomeLoanInterestCertificateData(BaseModel):
    document_type: str
    borrower_name: str | None = None
    pan: str | None = None
    co_borrower_name: str | None = None
    lender_name: str | None = None
    loan_account_number: str | None = None
    property_address: str | None = None
    financial_year: str | None = None
    loan_sanction_date: str | None = None
    possession_date: str | None = None
    loan_outstanding_opening: float | None = None
    principal_repaid: float | None = None
    interest_paid: float | None = None
    loan_outstanding_closing: float | None = None
    pre_emi_interest: float | None = None
    REQUIRED_FIELDS: ClassVar[list[str]] = ['borrower_name', 'pan', 'financial_year', 'interest_paid', 'principal_repaid']
