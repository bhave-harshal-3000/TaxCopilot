from typing import ClassVar
from pydantic import BaseModel


class LotteryWinningsStatementData(BaseModel):
    document_type: str
    winner_name: str | None = None
    pan: str | None = None
    financial_year: str | None = None
    source: str | None = None
    lottery_organizer: str | None = None
    gross_winnings: float | None = None
    tds_deducted_194b: float | None = None
    net_winnings_received: float | None = None
    prize_date: str | None = None
    REQUIRED_FIELDS: ClassVar[list[str]] = ['winner_name', 'pan', 'financial_year', 'gross_winnings']
