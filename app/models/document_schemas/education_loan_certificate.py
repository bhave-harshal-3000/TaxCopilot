from typing import ClassVar
from pydantic import BaseModel


class EducationLoanCertificateData(BaseModel):
    document_type: str
    borrower_name: str | None = None
    pan: str | None = None
    bank_name: str | None = None
    loan_account_number: str | None = None
    financial_year: str | None = None
    student_name: str | None = None
    course_name: str | None = None
    institution_name: str | None = None
    loan_disbursement_date: str | None = None
    interest_paid: float | None = None
    principal_paid: float | None = None
    outstanding_balance: float | None = None
    deduction_under_80e: float | None = None
    REQUIRED_FIELDS: ClassVar[list[str]] = ['borrower_name', 'pan', 'financial_year', 'interest_paid']
