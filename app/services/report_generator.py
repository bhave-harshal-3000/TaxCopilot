from app.models.financial_profile import FinancialProfile
from app.models.tax_result import TaxResult
from app.models.explanation_result import ExplanationResult
from app.models.tax_report import TaxReport


class ReportGenerator:

    @staticmethod
    def generate(
        profile: FinancialProfile,
        result: TaxResult,
        explanation: ExplanationResult
    ) -> TaxReport:

        taxpayer_info = {
            "taxpayer_name": profile.taxpayer_name,
            "pan": profile.pan,
            "financial_year": profile.financial_year,
        }

        income_summary = {
            "salary_income": profile.salary_income,
            "business_income": profile.business_income,
            "professional_income": profile.professional_income,
            "rental_income": profile.rental_income,
            "interest_income": profile.interest_income,
            "dividend_income": profile.dividend_income,
            "short_term_capital_gains": profile.stcg,
            "long_term_capital_gains": profile.ltcg,
            "crypto_income": profile.crypto_income,
            "foreign_income": profile.foreign_income,
            "agricultural_income": profile.agricultural_income,
        }

        deductions_summary = {
            "section_80c": profile.deduction_80c,
            "section_80d": profile.deduction_80d,
            "section_80e": profile.deduction_80e,
            "section_80g": profile.deduction_80g,
            "hra_exemption": profile.hra_exemption,
            "total_deductions": result.total_deductions,
        }

        tax_summary = {
            "gross_total_income": result.gross_total_income,
            "total_deductions": result.total_deductions,
            "taxable_income": result.taxable_income,
            "tax_before_rebate": result.tax_before_rebate,
            "rebate": result.rebate,
            "cess": result.cess,
            "total_tax_liability": result.total_tax_liability,
        }

        refund_or_payable = {
            "tds": result.tds,
            "advance_tax": result.advance_tax,
            "self_assessment_tax": result.self_assessment_tax,
            "total_taxes_paid": (
                result.tds
                + result.advance_tax
                + result.self_assessment_tax
            ),
            "tax_payable": result.tax_payable,
            "refund": result.refund,
        }

        return TaxReport(
            taxpayer_info=taxpayer_info,
            income_summary=income_summary,
            deductions_summary=deductions_summary,
            tax_summary=tax_summary,
            refund_or_payable=refund_or_payable,
            ai_explanation=explanation,
        )
