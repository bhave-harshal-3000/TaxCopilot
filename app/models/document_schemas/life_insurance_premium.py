from typing import ClassVar
from pydantic import BaseModel


class LifeInsurancePremiumData(BaseModel):
    document_type: str
    policyholder_name: str | None = None
    pan: str | None = None
    policy_number: str | None = None
    insurer_name: str | None = None
    policy_type: str | None = None
    financial_year: str | None = None
    annual_premium_paid: float | None = None
    sum_assured: float | None = None
    policy_start_date: str | None = None
    policy_maturity_date: str | None = None
    eligible_deduction_80c: float | None = None
    life_insured_name: str | None = None
    relationship_to_policyholder: str | None = None
    REQUIRED_FIELDS: ClassVar[list[str]] = ['policyholder_name', 'policy_number', 'financial_year', 'annual_premium_paid']
