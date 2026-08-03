from typing import ClassVar
from pydantic import BaseModel


class AgriculturalIncomeStatementData(BaseModel):
    document_type: str
    taxpayer_name: str | None = None
    pan: str | None = None
    financial_year: str | None = None
    land_location: str | None = None
    land_area_acres: float | None = None
    land_ownership_type: str | None = None
    crop_type: str | None = None
    gross_agricultural_receipts: float | None = None
    agricultural_expenses: float | None = None
    net_agricultural_income: float | None = None
    agricultural_income_exempt: bool | None = None
    used_for_partial_integration: bool | None = None
    REQUIRED_FIELDS: ClassVar[list[str]] = ['taxpayer_name', 'pan', 'financial_year', 'net_agricultural_income']
