from typing import ClassVar
from pydantic import BaseModel


class PartnershipIncomeStatementData(BaseModel):
    document_type: str
    partner_name: str | None = None
    partner_pan: str | None = None
    firm_name: str | None = None
    firm_pan: str | None = None
    financial_year: str | None = None
    profit_sharing_ratio: float | None = None
    share_in_firm_profit_loss: float | None = None
    remuneration_from_firm: float | None = None
    interest_on_capital_from_firm: float | None = None
    partner_capital_contribution: float | None = None
    exempt_share_of_profit: float | None = None
    taxable_remuneration: float | None = None
    REQUIRED_FIELDS: ClassVar[list[str]] = ['partner_name', 'partner_pan', 'firm_name', 'financial_year']
