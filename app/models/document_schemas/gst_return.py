from typing import ClassVar
from pydantic import BaseModel


class GSTReturnData(BaseModel):
    document_type: str
    taxpayer_name: str | None = None
    gstin: str | None = None
    pan: str | None = None
    financial_year: str | None = None
    return_type: str | None = None
    filing_period: str | None = None
    total_outward_supplies: float | None = None
    taxable_outward_supplies: float | None = None
    exempt_outward_supplies: float | None = None
    total_inward_supplies: float | None = None
    total_tax_liability: float | None = None
    cgst_liability: float | None = None
    sgst_liability: float | None = None
    igst_liability: float | None = None
    input_tax_credit_availed: float | None = None
    net_tax_payable: float | None = None
    annual_aggregate_turnover: float | None = None
    REQUIRED_FIELDS: ClassVar[list[str]] = ['taxpayer_name', 'gstin', 'financial_year', 'total_outward_supplies']
