from typing import ClassVar
from pydantic import BaseModel


class CryptoTransactionStatementData(BaseModel):
    document_type: str
    taxpayer_name: str | None = None
    pan: str | None = None
    exchange_name: str | None = None
    financial_year: str | None = None
    total_buy_value: float | None = None
    total_sell_value: float | None = None
    total_gain: float | None = None
    total_loss: float | None = None
    net_gain_loss: float | None = None
    tds_deducted_194s: float | None = None
    number_of_transactions: int | None = None
    currencies_traded: list | None = None
    transfer_of_vda_taxable_30_percent: float | None = None
    REQUIRED_FIELDS: ClassVar[list[str]] = ['taxpayer_name', 'pan', 'financial_year', 'total_sell_value']
