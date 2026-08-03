from typing import ClassVar
from pydantic import BaseModel


class TISData(BaseModel):
    document_type: str
    taxpayer_name: str | None = None
    pan: str | None = None
    financial_year: str | None = None
    salary_reported_ais: float | None = None
    salary_accepted_by_taxpayer: float | None = None
    interest_reported_ais: float | None = None
    interest_accepted_by_taxpayer: float | None = None
    dividend_reported_ais: float | None = None
    dividend_accepted_by_taxpayer: float | None = None
    capital_gains_reported_ais: float | None = None
    capital_gains_accepted_by_taxpayer: float | None = None
    other_income_reported_ais: float | None = None
    other_income_accepted_by_taxpayer: float | None = None
    taxpayer_modification_remarks: str | None = None
    REQUIRED_FIELDS: ClassVar[list[str]] = ['taxpayer_name', 'pan', 'financial_year']
