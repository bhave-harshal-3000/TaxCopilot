from pydantic import BaseModel
from app.models.explanation_result import ExplanationResult


class TaxReport(BaseModel):

    taxpayer_info: dict
    income_summary: dict
    deductions_summary: dict
    tax_summary: dict
    refund_or_payable: dict
    ai_explanation: ExplanationResult
