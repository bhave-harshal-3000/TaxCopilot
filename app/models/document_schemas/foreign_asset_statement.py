from typing import ClassVar
from pydantic import BaseModel


class ForeignAssetStatementData(BaseModel):
    document_type: str
    taxpayer_name: str | None = None
    pan: str | None = None
    financial_year: str | None = None
    country_of_asset: str | None = None
    asset_type: str | None = None
    foreign_bank_account_number: str | None = None
    foreign_bank_name: str | None = None
    peak_balance_foreign_currency: float | None = None
    peak_balance_inr: float | None = None
    closing_balance_inr: float | None = None
    foreign_equity_value_inr: float | None = None
    immovable_property_value_inr: float | None = None
    foreign_income_earned_inr: float | None = None
    foreign_tax_paid_inr: float | None = None
    dtaa_benefit_claimed: bool | None = None
    foreign_tax_credit_form_67: bool | None = None
    REQUIRED_FIELDS: ClassVar[list[str]] = ['taxpayer_name', 'pan', 'financial_year']
