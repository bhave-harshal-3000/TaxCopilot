from typing import ClassVar
from pydantic import BaseModel


class CapitalGainsStatementData(BaseModel):
    document_type: str
    taxpayer_name: str | None = None
    pan: str | None = None
    financial_year: str | None = None
    stcg_equity_15_percent: float | None = None
    ltcg_equity_10_percent: float | None = None
    stcg_debt_slab_rate: float | None = None
    ltcg_debt_20_percent_indexation: float | None = None
    stcg_property: float | None = None
    ltcg_property_20_percent_indexation: float | None = None
    stcg_mutual_funds: float | None = None
    ltcg_mutual_funds: float | None = None
    total_stcg: float | None = None
    total_ltcg: float | None = None
    set_off_losses: float | None = None
    net_capital_gains: float | None = None
    indexation_benefit_claimed: float | None = None
    REQUIRED_FIELDS: ClassVar[list[str]] = ['taxpayer_name', 'pan', 'financial_year', 'net_capital_gains']
