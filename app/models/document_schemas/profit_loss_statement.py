from typing import ClassVar
from pydantic import BaseModel


class ProfitLossStatementData(BaseModel):
    document_type: str
    business_name: str | None = None
    pan: str | None = None
    financial_year: str | None = None
    total_revenue: float | None = None
    cost_of_goods_sold: float | None = None
    gross_profit: float | None = None
    employee_expenses: float | None = None
    rent_expense: float | None = None
    depreciation: float | None = None
    interest_expense: float | None = None
    other_operating_expenses: float | None = None
    total_operating_expenses: float | None = None
    net_profit_before_tax: float | None = None
    tax_expense: float | None = None
    net_profit_after_tax: float | None = None
    REQUIRED_FIELDS: ClassVar[list[str]] = ['business_name', 'financial_year', 'total_revenue', 'net_profit_after_tax']
