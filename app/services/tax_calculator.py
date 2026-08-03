from app.models.financial_profile import FinancialProfile
from app.models.tax_result import TaxResult


class TaxCalculator:

    @staticmethod
    def calculate(profile: FinancialProfile,regime: str = "new") -> TaxResult:

        result = TaxResult()


        # Gross Total Income

        result.gross_total_income = (
            profile.salary_income
            + profile.business_income
            + profile.professional_income
            + profile.rental_income
            + profile.interest_income
            + profile.dividend_income
            + profile.stcg
            + profile.ltcg
            + profile.crypto_income
            + profile.foreign_income
            + profile.agricultural_income
        )

        # Deductions

        result.total_deductions = (
            profile.deduction_80c
            + profile.deduction_80d
            + profile.deduction_80e
            + profile.deduction_80g
            + profile.hra_exemption
        )

        result.taxable_income = max(0,
            result.gross_total_income
            - result.total_deductions
        )

        # Calculate Tax

        if regime.lower() == "new":
            result.tax_before_rebate = TaxCalculator.calculate_new_regime_tax(result.taxable_income)
        else:
            result.tax_before_rebate = TaxCalculator.calculate_old_regime_tax(result.taxable_income)

        # Rebate (placeholder)

        result.rebate = 0

        # Health & Education Cess

        result.cess = result.tax_before_rebate * 0.04

        result.total_tax_liability = (
            result.tax_before_rebate
            + result.cess
            - result.rebate
        )

        # Taxes already paid

        result.tds = profile.tds
        result.advance_tax = profile.advance_tax
        result.self_assessment_tax = profile.self_assessment_tax

        taxes_paid = (
            result.tds
            + result.advance_tax
            + result.self_assessment_tax
        )

        if taxes_paid >= result.total_tax_liability:
            result.refund = (taxes_paid - result.total_tax_liability)

        else:
            result.tax_payable = (result.total_tax_liability - taxes_paid)

        return result

    #------------------------------- NEW REGIME (placeholder) -------------------------------------

    @staticmethod
    def calculate_new_regime_tax(income: float) -> float:

        tax = 0

        if income <= 400000:
            return 0

        slabs = [
            (400000, 800000, 0.05),
            (800000, 1200000, 0.10),
            (1200000, 1600000, 0.15),
            (1600000, 2000000, 0.20),
            (2000000, 2400000, 0.25),
            (2400000, float("inf"), 0.30)
        ]

        for lower, upper, rate in slabs:
            if income > lower:
                taxable = min(income, upper) - lower
                tax += taxable * rate
        return tax

    #------------------------------- OLD REGIME (placeholder) -------------------------------------

    @staticmethod
    def calculate_old_regime_tax(income: float) -> float:

        tax = 0

        if income <= 250000:
            return 0

        slabs = [
            (250000, 500000, 0.05),
            (500000, 1000000, 0.20),
            (1000000, float("inf"), 0.30)
        ]

        for lower, upper, rate in slabs:
            if income > lower:
                taxable = min(income, upper) - lower
                tax += taxable * rate

        return tax