

from dataclasses import dataclass
from pathlib import Path
from src.strategy_system.stocks.stock.components.IncomeStatement import IncomeStatement
from src.strategy_system.stocks.stock.components.Earnings import EarningsStatement
from src.strategy_system.stocks.stock.components.BalanceSheet import BalanceSheet
from src.strategy_system.stocks.stock.components.CashFlow import CashFlow
from src.strategy_system.stocks.stock.components.CompanyOverview import CompanyOverview
from src.strategy_system.stocks import calculators as calcs
from src.strategy_system.stocks.calculators import GrahamNumberCalculator

PATH_TO_STOCK_DATA = Path(
    "./scripts/SimpleAlphaVantageCacher/output/json_cache/DATA")


@dataclass
class Stock:

    ticker: str
    income_statement: IncomeStatement
    earnings: Earnings
    balance_sheet: BalanceSheet
    cash_flow: CashFlow
    company_overview: CompanyOverview
    last_updated = None
    symbol = None
    intrinsic_value = None

    @classmethod
    def from_ticker(cls, ticker: str):
        pass

    @classmethod
    def from_alpha_vantage_data(cls, ticker: str):

        income_statement: IncomeStatement = IncomeStatement.from_json_file()
        earnings: EarningsStatement = EarningsStatement.from_json_file()
        balance_sheet: BalanceSheet = BalanceSheet.from_json_file()
        cash_flow: CashFlow = CashFlow.from_json_file()
        company_overview: CompanyOverview = CompanyOverview.from_json_file()

        cls(ticker, income_statement, earnings,
            balance_sheet, cash_flow, company_overview)

    @staticmethod
    def earnings_file_path(ticker: str):
        path = PATH_TO_STOCK_DATA/f"{ticker}.Earnings.json"
        if not path.exists():
            raise

    @property
    def graham_number(self):
        GrahamNumberCalculator(self).run()


def build_paths(ticker: str):
    income_statement_file_name = f"{ticker}.IncomeStatement.json"
    earnings_file_name = f"{ticker}.Earnings.json"
    balance_sheet_file_name = f"{ticker}.BalanceSheet.json"
    cash_flow_file_name = f"{ticker}.CashFlow.json"
    company_overview_file_name = f"{ticker}.CompanyOverview.json"
