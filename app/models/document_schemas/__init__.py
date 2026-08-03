# app/models/document_schemas/__init__.py
# Exports all 45 Pydantic document schema models.
# Import from here when building the DOCUMENT_SCHEMAS registry.

from app.models.document_schemas.form16 import Form16Data
from app.models.document_schemas.form16a import Form16AData
from app.models.document_schemas.form26as import Form26ASData
from app.models.document_schemas.ais import AISData
from app.models.document_schemas.tis import TISData

from app.models.document_schemas.salary_slip import SalarySlipData
from app.models.document_schemas.pension_statement import PensionStatementData
from app.models.document_schemas.gratuity_statement import GratuityStatementData

from app.models.document_schemas.epf_statement import EPFStatementData
from app.models.document_schemas.ppf_passbook import PPFPassbookData
from app.models.document_schemas.nps_statement import NPSStatementData
from app.models.document_schemas.elss_statement import ELSSStatementData
from app.models.document_schemas.ulip_statement import ULIPStatementData

from app.models.document_schemas.bank_statement import BankStatementData
from app.models.document_schemas.fd_interest_certificate import FDInterestCertificateData
from app.models.document_schemas.savings_interest_certificate import SavingsInterestCertificateData

from app.models.document_schemas.broker_statement import BrokerStatementData
from app.models.document_schemas.mutual_fund_cas import MutualFundCASData
from app.models.document_schemas.demat_statement import DematStatementData
from app.models.document_schemas.dividend_statement import DividendStatementData
from app.models.document_schemas.capital_gains_statement import CapitalGainsStatementData

from app.models.document_schemas.home_loan_interest_certificate import HomeLoanInterestCertificateData
from app.models.document_schemas.rental_income_statement import RentalIncomeStatementData
from app.models.document_schemas.rent_receipts import RentReceiptsData

from app.models.document_schemas.life_insurance_premium import LifeInsurancePremiumData
from app.models.document_schemas.medical_insurance_80d import MedicalInsurance80DData

from app.models.document_schemas.donation_receipt_80g import DonationReceipt80GData
from app.models.document_schemas.education_loan_certificate import EducationLoanCertificateData
from app.models.document_schemas.tuition_fee_receipt import TuitionFeeReceiptData
from app.models.document_schemas.hra_declaration import HRADeclarationData

from app.models.document_schemas.rsu_statement import RSUStatementData
from app.models.document_schemas.esop_statement import ESOPStatementData
from app.models.document_schemas.crypto_transaction_statement import CryptoTransactionStatementData
from app.models.document_schemas.foreign_asset_statement import ForeignAssetStatementData

from app.models.document_schemas.gst_return import GSTReturnData
from app.models.document_schemas.profit_loss_statement import ProfitLossStatementData
from app.models.document_schemas.balance_sheet import BalanceSheetData
from app.models.document_schemas.business_income_statement import BusinessIncomeStatementData
from app.models.document_schemas.professional_income_statement import ProfessionalIncomeStatementData
from app.models.document_schemas.partnership_income_statement import PartnershipIncomeStatementData
from app.models.document_schemas.agricultural_income_statement import AgriculturalIncomeStatementData

from app.models.document_schemas.freelancer_invoice import FreelancerInvoiceData
from app.models.document_schemas.speculative_income_statement import SpeculativeIncomeStatementData
from app.models.document_schemas.lottery_winnings_statement import LotteryWinningsStatementData
from app.models.document_schemas.foreign_income_statement import ForeignIncomeStatementData

__all__ = [
    "Form16Data",
    "Form16AData",
    "Form26ASData",
    "AISData",
    "TISData",
    "SalarySlipData",
    "PensionStatementData",
    "GratuityStatementData",
    "EPFStatementData",
    "PPFPassbookData",
    "NPSStatementData",
    "ELSSStatementData",
    "ULIPStatementData",
    "BankStatementData",
    "FDInterestCertificateData",
    "SavingsInterestCertificateData",
    "BrokerStatementData",
    "MutualFundCASData",
    "DematStatementData",
    "DividendStatementData",
    "CapitalGainsStatementData",
    "HomeLoanInterestCertificateData",
    "RentalIncomeStatementData",
    "RentReceiptsData",
    "LifeInsurancePremiumData",
    "MedicalInsurance80DData",
    "DonationReceipt80GData",
    "EducationLoanCertificateData",
    "TuitionFeeReceiptData",
    "HRADeclarationData",
    "RSUStatementData",
    "ESOPStatementData",
    "CryptoTransactionStatementData",
    "ForeignAssetStatementData",
    "GSTReturnData",
    "ProfitLossStatementData",
    "BalanceSheetData",
    "BusinessIncomeStatementData",
    "ProfessionalIncomeStatementData",
    "PartnershipIncomeStatementData",
    "AgriculturalIncomeStatementData",
    "FreelancerInvoiceData",
    "SpeculativeIncomeStatementData",
    "LotteryWinningsStatementData",
    "ForeignIncomeStatementData",
]
