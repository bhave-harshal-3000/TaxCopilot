from pydantic import BaseModel


class ExplanationResult(BaseModel):

    income_summary: str = ""
    deductions_summary: str = ""
    tax_computation: str = ""
    refund_or_payable: str = ""
    recommendations: list[str] = []
