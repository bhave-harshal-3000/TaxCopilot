from typing import ClassVar
from pydantic import BaseModel


class GratuityStatementData(BaseModel):
    document_type: str
    employee_name: str | None = None
    pan: str | None = None
    employer_name: str | None = None
    date_of_joining: str | None = None
    date_of_leaving: str | None = None
    years_of_service: float | None = None
    last_drawn_salary: float | None = None
    gratuity_amount_received: float | None = None
    exempt_gratuity: float | None = None
    taxable_gratuity: float | None = None
    tds_deducted: float | None = None
    REQUIRED_FIELDS: ClassVar[list[str]] = ['employee_name', 'pan', 'gratuity_amount_received']
