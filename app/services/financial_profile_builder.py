from app.models.financial_profile import FinancialProfile

from app.models.document_schemas import (
    Form16Data,
    AISData,
    BrokerStatementData,
    BankStatementData,
    BusinessIncomeStatementData,
    ProfessionalIncomeStatementData,
    RentalIncomeStatementData,
    ForeignIncomeStatementData,
    MedicalInsurance80DData,
    DonationReceipt80GData,
    EducationLoanCertificateData,
)


class FinancialProfileBuilder:

    @staticmethod
    def build(parsed_documents: list):

        profile = FinancialProfile()

        for document in parsed_documents:

  
            # Form 16
 
            if isinstance(document, Form16Data):

                profile.taxpayer_name = document.employee_name
                profile.pan = document.employee_pan
                profile.financial_year = document.financial_year

                profile.salary_income += document.gross_salary or 0
                profile.tds += document.tds_deducted or 0

            
            # AIS
            
            elif isinstance(document, AISData):

                profile.interest_income += (
                    document.interest_income_deposits or 0
                )

                profile.dividend_income += (
                    document.dividend_income or 0
                )

                profile.advance_tax += (
                    document.total_tax_paid or 0
                )

            
            # Broker Statement
        
            elif isinstance(document, BrokerStatementData):

                profile.stcg += (
                    document.short_term_capital_gain or 0
                )

                profile.ltcg += (
                    document.long_term_capital_gain or 0
                )

            
            # Bank Statement
            
            elif isinstance(document, BankStatementData):

                profile.interest_income += (
                    document.total_interest or 0
                )

            
            # Business
            
            elif isinstance(document, BusinessIncomeStatementData):

                profile.business_income += (
                    document.business_income or 0
                )

            
            # Professional
            
            elif isinstance(document, ProfessionalIncomeStatementData):

                profile.professional_income += (
                    document.professional_income or 0
                )

            
            # Rental
            
            elif isinstance(document, RentalIncomeStatementData):

                profile.rental_income += (
                    document.rental_income or 0
                )

            
            # Foreign
            
            elif isinstance(document, ForeignIncomeStatementData):

                profile.foreign_income += (
                    document.foreign_income or 0
                )

            # Deductions
            elif isinstance(document, MedicalInsurance80DData):

                profile.deduction_80d += (
                    document.premium_paid or 0
                )

            elif isinstance(document, DonationReceipt80GData):

                profile.deduction_80g += (
                    document.donation_amount or 0
                )

            elif isinstance(document, EducationLoanCertificateData):

                profile.deduction_80e += (
                    document.interest_paid or 0
                )

        return profile