from typing import ClassVar
from pydantic import BaseModel


class DematStatementData(BaseModel):
    document_type: str
    account_holder_name: str | None = None
    pan: str | None = None
    demat_account_number: str | None = None
    depository: str | None = None
    depository_participant: str | None = None
    as_on_date: str | None = None
    total_holdings_value: float | None = None
    equity_holdings_value: float | None = None
    mutual_fund_holdings_value: float | None = None
    bonds_debentures_value: float | None = None
    etf_value: float | None = None
    number_of_scrips: int | None = None
    REQUIRED_FIELDS: ClassVar[list[str]] = ['account_holder_name', 'demat_account_number', 'as_on_date', 'total_holdings_value']
