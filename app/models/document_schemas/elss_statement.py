from typing import ClassVar
from pydantic import BaseModel


class ELSSStatementData(BaseModel):
    document_type: str
    investor_name: str | None = None
    pan: str | None = None
    financial_year: str | None = None
    fund_name: str | None = None
    folio_number: str | None = None
    amount_invested: float | None = None
    units_purchased: float | None = None
    nav_at_purchase: float | None = None
    purchase_date: str | None = None
    lock_in_expiry_date: str | None = None
    current_nav: float | None = None
    current_value: float | None = None
    unrealised_gain_loss: float | None = None
    deduction_under_80c: float | None = None
    REQUIRED_FIELDS: ClassVar[list[str]] = ['investor_name', 'pan', 'financial_year', 'amount_invested']
