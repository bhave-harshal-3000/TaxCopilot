from typing import ClassVar
from pydantic import BaseModel


class RSUStatementData(BaseModel):
    document_type: str
    employee_name: str | None = None
    pan: str | None = None
    employer_name: str | None = None
    company_name: str | None = None
    financial_year: str | None = None
    rsus_vested: int | None = None
    vesting_date: str | None = None
    fair_market_value_on_vesting: float | None = None
    total_perquisite_value: float | None = None
    tds_on_perquisite: float | None = None
    rsus_sold: int | None = None
    sale_date: str | None = None
    sale_price_per_unit: float | None = None
    total_sale_proceeds: float | None = None
    capital_gain_loss: float | None = None
    holding_period: str | None = None
    REQUIRED_FIELDS: ClassVar[list[str]] = ['employee_name', 'pan', 'financial_year']
