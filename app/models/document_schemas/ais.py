from typing import ClassVar
from pydantic import BaseModel


class AISData(BaseModel):
    document_type: str
    taxpayer_name: str | None = None
    pan: str | None = None
    financial_year: str | None = None
    salary_income: float | None = None
    interest_income_savings: float | None = None
    interest_income_deposits: float | None = None
    dividend_income: float | None = None
    securities_sale_value: float | None = None
    mutual_fund_sale_value: float | None = None
    foreign_remittance_received: float | None = None
    rent_received: float | None = None
    total_tds: float | None = None
    total_tax_paid: float | None = None
    gst_turnover: float | None = None
    REQUIRED_FIELDS: ClassVar[list[str]] = ['taxpayer_name', 'pan', 'financial_year']
