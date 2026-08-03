from typing import ClassVar
from pydantic import BaseModel


class DividendStatementData(BaseModel):
    document_type: str
    shareholder_name: str | None = None
    pan: str | None = None
    financial_year: str | None = None
    company_name: str | None = None
    isin: str | None = None
    number_of_shares: int | None = None
    dividend_per_share: float | None = None
    total_dividend_received: float | None = None
    tds_deducted: float | None = None
    net_dividend_received: float | None = None
    dividend_payment_date: str | None = None
    REQUIRED_FIELDS: ClassVar[list[str]] = ['shareholder_name', 'pan', 'financial_year', 'total_dividend_received']
