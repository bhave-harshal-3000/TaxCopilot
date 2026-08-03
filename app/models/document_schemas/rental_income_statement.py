from typing import ClassVar
from pydantic import BaseModel


class RentalIncomeStatementData(BaseModel):
    document_type: str
    owner_name: str | None = None
    pan: str | None = None
    financial_year: str | None = None
    property_address: str | None = None
    property_type: str | None = None
    tenant_name: str | None = None
    tenant_pan: str | None = None
    annual_rent_received: float | None = None
    municipal_taxes_paid: float | None = None
    net_annual_value: float | None = None
    standard_deduction_30_percent: float | None = None
    home_loan_interest_deduction: float | None = None
    net_taxable_rental_income: float | None = None
    tds_deducted_by_tenant: float | None = None
    REQUIRED_FIELDS: ClassVar[list[str]] = ['owner_name', 'pan', 'financial_year', 'annual_rent_received']
