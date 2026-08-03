from typing import ClassVar
from pydantic import BaseModel


class ForeignIncomeStatementData(BaseModel):
    document_type: str
    taxpayer_name: str | None = None
    pan: str | None = None
    financial_year: str | None = None
    country_of_income: str | None = None
    nature_of_income: str | None = None
    gross_foreign_income_foreign_currency: float | None = None
    currency_code: str | None = None
    exchange_rate_used: float | None = None
    gross_foreign_income_inr: float | None = None
    foreign_tax_paid_inr: float | None = None
    dtaa_article_applicable: str | None = None
    dtaa_relief_claimed: float | None = None
    form_67_filed: bool | None = None
    net_income_taxable_in_india: float | None = None
    REQUIRED_FIELDS: ClassVar[list[str]] = ['taxpayer_name', 'pan', 'financial_year', 'gross_foreign_income_inr']
