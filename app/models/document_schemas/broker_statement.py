from typing import ClassVar
from pydantic import BaseModel


class BrokerStatementData(BaseModel):
    document_type: str
    client_name: str | None = None
    pan: str | None = None
    broker_name: str | None = None
    demat_account_number: str | None = None
    financial_year: str | None = None
    total_buy_value: float | None = None
    total_sell_value: float | None = None
    short_term_capital_gain: float | None = None
    long_term_capital_gain: float | None = None
    speculative_profit_loss: float | None = None
    intraday_profit_loss: float | None = None
    fno_profit_loss: float | None = None
    brokerage_paid: float | None = None
    stt_paid: float | None = None
    total_turnover: float | None = None
    REQUIRED_FIELDS: ClassVar[list[str]] = ['client_name', 'pan', 'financial_year', 'total_turnover']
