from typing import ClassVar
from pydantic import BaseModel


class ESOPStatementData(BaseModel):
    document_type: str
    employee_name: str | None = None
    pan: str | None = None
    employer_name: str | None = None
    company_name: str | None = None
    financial_year: str | None = None
    options_granted: int | None = None
    options_vested: int | None = None
    options_exercised: int | None = None
    exercise_date: str | None = None
    exercise_price_per_share: float | None = None
    fair_market_value_on_exercise: float | None = None
    perquisite_value: float | None = None
    tds_on_perquisite: float | None = None
    shares_sold: int | None = None
    sale_date: str | None = None
    sale_price_per_share: float | None = None
    capital_gain_loss: float | None = None
    holding_period: str | None = None
    REQUIRED_FIELDS: ClassVar[list[str]] = ['employee_name', 'pan', 'financial_year']
