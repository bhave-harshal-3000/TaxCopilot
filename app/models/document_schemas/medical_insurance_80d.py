from typing import ClassVar
from pydantic import BaseModel


class MedicalInsurance80DData(BaseModel):
    document_type: str
    policyholder_name: str | None = None
    pan: str | None = None
    insurer_name: str | None = None
    policy_number: str | None = None
    financial_year: str | None = None
    premium_self_spouse_children: float | None = None
    premium_parents: float | None = None
    preventive_health_checkup_self: float | None = None
    preventive_health_checkup_parents: float | None = None
    parents_are_senior_citizens: bool | None = None
    self_is_senior_citizen: bool | None = None
    total_deduction_80d: float | None = None
    REQUIRED_FIELDS: ClassVar[list[str]] = ['policyholder_name', 'financial_year', 'premium_self_spouse_children']
