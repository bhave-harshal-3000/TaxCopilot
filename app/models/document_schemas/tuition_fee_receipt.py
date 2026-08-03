from typing import ClassVar
from pydantic import BaseModel


class TuitionFeeReceiptData(BaseModel):
    document_type: str
    parent_name: str | None = None
    pan: str | None = None
    student_name: str | None = None
    institution_name: str | None = None
    institution_address: str | None = None
    financial_year: str | None = None
    academic_year: str | None = None
    tuition_fee_paid: float | None = None
    other_fees_paid: float | None = None
    receipt_number: str | None = None
    eligible_for_80c: bool | None = None
    REQUIRED_FIELDS: ClassVar[list[str]] = ['parent_name', 'student_name', 'tuition_fee_paid', 'financial_year']
