from typing import ClassVar
from pydantic import BaseModel


class Form16Data(BaseModel):
    document_type: str
    employee_name: str | None = None
    employee_pan: str | None = None
    employer_name: str | None = None
    employer_tan: str | None = None
    financial_year: str | None = None
    assessment_year: str | None = None
    gross_salary: float | None = None
    basic_salary: float | None = None
    hra_received: float | None = None
    special_allowance: float | None = None
    other_allowances: float | None = None
    professional_tax: float | None = None
    standard_deduction: float | None = None
    net_taxable_salary: float | None = None
    tds_deducted: float | None = None
    total_tds_deposited: float | None = None
    REQUIRED_FIELDS: ClassVar[list[str]] = ['employee_name', 'employee_pan', 'financial_year', 'gross_salary', 'tds_deducted']
