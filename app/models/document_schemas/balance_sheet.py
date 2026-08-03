from typing import ClassVar
from pydantic import BaseModel


class BalanceSheetData(BaseModel):
    document_type: str
    entity_name: str | None = None
    pan: str | None = None
    as_on_date: str | None = None
    total_assets: float | None = None
    fixed_assets_net: float | None = None
    capital_work_in_progress: float | None = None
    investments: float | None = None
    inventories: float | None = None
    trade_receivables: float | None = None
    cash_and_bank_balances: float | None = None
    other_current_assets: float | None = None
    total_liabilities: float | None = None
    long_term_borrowings: float | None = None
    short_term_borrowings: float | None = None
    trade_payables: float | None = None
    other_current_liabilities: float | None = None
    partner_capital: float | None = None
    reserves_and_surplus: float | None = None
    REQUIRED_FIELDS: ClassVar[list[str]] = ['entity_name', 'as_on_date', 'total_assets', 'total_liabilities']
