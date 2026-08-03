from typing import ClassVar
from pydantic import BaseModel


class SpeculativeIncomeStatementData(BaseModel):
    document_type: str
    taxpayer_name: str | None = None
    pan: str | None = None
    financial_year: str | None = None
    broker_name: str | None = None
    total_speculative_turnover: float | None = None
    total_speculative_profit: float | None = None
    total_speculative_loss: float | None = None
    net_speculative_income: float | None = None
    number_of_trades: int | None = None
    stt_paid: float | None = None
    set_off_from_other_speculative_years: float | None = None
    REQUIRED_FIELDS: ClassVar[list[str]] = ['taxpayer_name', 'pan', 'financial_year', 'net_speculative_income']
