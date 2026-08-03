from typing import ClassVar
from pydantic import BaseModel


class MutualFundCASData(BaseModel):
    document_type: str
    investor_name: str | None = None
    pan: str | None = None
    email: str | None = None
    financial_year: str | None = None
    number_of_folios: int | None = None
    total_invested: float | None = None
    total_redeemed: float | None = None
    current_value: float | None = None
    unrealised_gain_loss: float | None = None
    short_term_capital_gain: float | None = None
    long_term_capital_gain: float | None = None
    dividend_received: float | None = None
    tds_on_dividend: float | None = None
    exit_load_paid: float | None = None
    REQUIRED_FIELDS: ClassVar[list[str]] = ['investor_name', 'pan', 'financial_year', 'current_value']
