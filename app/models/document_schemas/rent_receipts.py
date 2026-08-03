from typing import ClassVar
from pydantic import BaseModel


class RentReceiptsData(BaseModel):
    document_type: str
    tenant_name: str | None = None
    landlord_name: str | None = None
    landlord_pan: str | None = None
    property_address: str | None = None
    city: str | None = None
    monthly_rent: float | None = None
    financial_year: str | None = None
    total_rent_paid: float | None = None
    period_from: str | None = None
    period_to: str | None = None
    REQUIRED_FIELDS: ClassVar[list[str]] = ['tenant_name', 'landlord_name', 'total_rent_paid', 'financial_year']
