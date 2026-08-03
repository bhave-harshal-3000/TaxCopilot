from typing import ClassVar
from pydantic import BaseModel


class ULIPStatementData(BaseModel):
    document_type: str
    policyholder_name: str | None = None
    pan: str | None = None
    policy_number: str | None = None
    insurer_name: str | None = None
    financial_year: str | None = None
    premium_paid: float | None = None
    sum_assured: float | None = None
    fund_value: float | None = None
    mortality_charges: float | None = None
    fund_management_charges: float | None = None
    maturity_date: str | None = None
    policy_start_date: str | None = None
    deduction_under_80c: float | None = None
    taxable_maturity_proceeds: float | None = None
    REQUIRED_FIELDS: ClassVar[list[str]] = ['policyholder_name', 'policy_number', 'financial_year', 'premium_paid']
