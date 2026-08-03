from pydantic import BaseModel


class TaxResult(BaseModel):

    gross_total_income: float = 0.0

    total_deductions: float = 0.0

    taxable_income: float = 0.0

    tax_before_rebate: float = 0.0

    rebate: float = 0.0

    cess: float = 0.0

    total_tax_liability: float = 0.0

    tds: float = 0.0

    advance_tax: float = 0.0

    self_assessment_tax: float = 0.0

    tax_payable: float = 0.0

    refund: float = 0.0