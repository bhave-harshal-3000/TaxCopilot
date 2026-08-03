from typing import ClassVar
from pydantic import BaseModel


class FreelancerInvoiceData(BaseModel):
    document_type: str
    freelancer_name: str | None = None
    pan: str | None = None
    gstin: str | None = None
    client_name: str | None = None
    client_pan: str | None = None
    invoice_number: str | None = None
    invoice_date: str | None = None
    financial_year: str | None = None
    services_rendered: str | None = None
    invoice_amount: float | None = None
    gst_charged: float | None = None
    tds_deducted: float | None = None
    net_amount_received: float | None = None
    REQUIRED_FIELDS: ClassVar[list[str]] = ['freelancer_name', 'pan', 'invoice_amount', 'financial_year']
