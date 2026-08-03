from typing import ClassVar
from pydantic import BaseModel


class SalarySlipData(BaseModel):
    document_type: str
    employee_name: str | None = None
    employee_id: str | None = None
    pan: str | None = None
    employer_name: str | None = None
    month: str | None = None
    year: str | None = None
    basic_salary: float | None = None
    hra: float | None = None
    special_allowance: float | None = None
    transport_allowance: float | None = None
    medical_allowance: float | None = None
    lta: float | None = None
    gross_earnings: float | None = None
    provident_fund_deduction: float | None = None
    esic_deduction: float | None = None
    professional_tax_deduction: float | None = None
    tds_deduction: float | None = None
    total_deductions: float | None = None
    net_pay: float | None = None
    REQUIRED_FIELDS: ClassVar[list[str]] = ['employee_name', 'pan', 'month', 'year', 'gross_earnings', 'net_pay']
