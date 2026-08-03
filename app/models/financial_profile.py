from pydantic import BaseModel


class FinancialProfile(BaseModel):

    # Identity
    taxpayer_name: str | None = None
    pan: str | None = None
    financial_year: str | None = None

    # Income
    salary_income: float = 0.0
    business_income: float = 0.0
    professional_income: float = 0.0
    rental_income: float = 0.0
    interest_income: float = 0.0
    dividend_income: float = 0.0
    stcg: float = 0.0
    ltcg: float = 0.0
    crypto_income: float = 0.0
    foreign_income: float = 0.0
    agricultural_income: float = 0.0

    # Deductions
    deduction_80c: float = 0.0
    deduction_80d: float = 0.0
    deduction_80e: float = 0.0
    deduction_80g: float = 0.0
    hra_exemption: float = 0.0

    # Taxes Paid
    tds: float = 0.0
    advance_tax: float = 0.0
    self_assessment_tax: float = 0.0