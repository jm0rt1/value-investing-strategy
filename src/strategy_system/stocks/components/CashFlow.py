

from src.strategy_system.stocks.components.StockComponent import StockComponent


from dataclasses import dataclass
from src.strategy_system.stocks.components.StockComponent import StockComponent


@dataclass
class CashFlowReport:
    fiscal_date_ending: str
    reported_currency: str
    operating_cashflow: float
    payments_for_operating_activities: float
    proceeds_from_operating_activities: float
    change_in_operating_liabilities: float
    change_in_operating_assets: float
    depreciation_depletion_and_amortization: float
    capital_expenditures: float
    investments: float
    other_cashflows_from_investing_activities: float
    total_cashflows_from_investing_activities: float
    dividends_paid: float
    net_cash_from_financing_activities: float
    change_in_cash_and_cash_equivalents: float
    effect_of_exchange_rate_changes: float
    net_income: float
    change_in_inventory: float
    change_in_account_receivables: float
    change_in_net_income: float
    capital_lease_obligations: float
    financing_cashflow: float
    dividends_received: float
    investment_purchases_and_sales: float
    investing_cashflow: float
    issuance_payments_of_debt: float
    issuance_payments_of_equity: float
    net_debt_issuance: float
    total_cash_from_financing_activities: float
    free_cash_flow: float

    @classmethod
    def from_dict(cls, data: dict[str, str]) -> 'CashFlowReport':
        return cls(
            fiscal_date_ending=data.get('fiscalDateEnding', ''),
            reported_currency=data.get('reportedCurrency', ''),
            operating_cashflow=float(data.get('operatingCashflow', '0')),
            payments_for_operating_activities=float(
                data.get('paymentsForOperatingActivities', '0')),
            proceeds_from_operating_activities=float(
                data.get('proceedsFromOperatingActivities', '0')),
            change_in_operating_liabilities=float(
                data.get('changeInOperatingLiabilities', '0')),
            change_in_operating_assets=float(
                data.get('changeInOperatingAssets', '0')),
            depreciation_depletion_and_amortization=float(
                data.get('depreciationDepletionAndAmortization', '0')),
            capital_expenditures=float(data.get('capitalExpenditures', '0')),
            investments=float(data.get('investments', '0')),
            other_cashflows_from_investing_activities=float(
                data.get('otherCashflowsFromInvestingActivities', '0')),
            total_cashflows_from_investing_activities=float(
                data.get('totalCashflowsFromInvestingActivities', '0')),
            dividends_paid=float(data.get('dividendsPaid', '0')),
            net_cash_from_financing_activities=float(
                data.get('netCashFromFinancingActivities', '0')),
            change_in_cash_and_cash_equivalents=float(
                data.get('changeInCashAndCashEquivalents', '0')),
            effect_of_exchange_rate_changes=float(
                data.get('effectOfExchangeRateChanges', '0')),
            net_income=float(data.get('netIncome', '0')),
            change_in_inventory=float(data.get('changeInInventory', '0')),
            change_in_account_receivables=float(
                data.get('changeInAccountReceivables', '0')),
            change_in_net_income=float(data.get('changeInNetIncome', '0')),
            capital_lease_obligations=float(
                data.get('capitalLeaseObligations', '0')),
            financing_cashflow=float(data.get('financingCashflow', '0')),
            dividends_received=float(data.get('dividendsReceived', '0')),
            investment_purchases_and_sales=float(
                data.get('investmentPurchasesAndSales', '0')),
            investing_cashflow=float(data.get('investingCashflow', '0')),
            issuance_payments_of_debt=float(
                data.get('issuancePaymentsOfDebt', '0')),
            issuance_payments_of_equity=float(
                data.get('issuancePaymentsOfEquity', '0')),
            net_debt_issuance=float(data.get('netDebtIssuance', '0')),
            total_cash_from_financing_activities=float(
                data.get('totalCashFromFinancingActivities', '0')),
            free_cash_flow=float(data.get('freeCashFlow', '0'))
        )


class CashFlow(StockComponent):
    pass
