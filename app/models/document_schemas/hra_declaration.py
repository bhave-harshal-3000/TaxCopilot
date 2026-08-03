from typing import ClassVar
from pydantic import BaseModel


class HRADeclarationData(BaseModel):
    document_type: str
    employee_name: str | None = None
    pan: str | None = None
    employer_name: str | None = None
    financial_year: str | None = None
    city_of_residence: str | None = None
    city_type: str | None = None
    basic_salary_annual: float | None = None
    hra_received_annual: float | None = None
    rent_paid_annual: float | None = None
    landlord_name: str | None = None
    landlord_pan: str | None = None
    landlord_address: str | None = None
    hra_exemption_calculated: float | None = None
    taxable_hra: float | None = None
    REQUIRED_FIELDS: ClassVar[list[str]] = ['employee_name', 'pan', 'financial_year', 'rent_paid_annual']
