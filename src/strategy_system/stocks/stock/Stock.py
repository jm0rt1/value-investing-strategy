

from src.strategy_system.stocks.components import IncomeStatement, EarningsReport, BalanceSheet, CashFlow, CompanyOverview
from src.strategy_system.stocks.calculators import SharpeRatioCalculator


class Stock:

    def __init__(self, ticker: str):
        self.last_updated = None
        self.symbol = None
        self.intrinsic_value = None
        self.ticker: str

    def from_alpha_vantage_data(self, income_statement: IncomeStatement, earnings: EarningsReport, balance_sheet: BalanceSheet, cash_flow: CashFlow, company_overview: CompanyOverview):
        pass
