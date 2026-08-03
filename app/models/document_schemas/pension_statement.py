from typing import ClassVar
from pydantic import BaseModel


class PensionStatementData(BaseModel):
    document_type: str
    pensioner_name: str | None = None
    pan: str | None = None
    pension_account_number: str | None = None
    financial_year: str | None = None
    pension_type: str | None = None
    monthly_pension: float | None = None
    annual_pension: float | None = None
    dearness_relief: float | None = None
    commuted_pension_received: float | None = None
    commuted_pension_exempt: float | None = None
    tds_deducted: float | None = None
    pension_paying_authority: str | None = None
    REQUIRED_FIELDS: ClassVar[list[str]] = ['pensioner_name', 'pan', 'financial_year', 'annual_pension']
