

from dataclasses import dataclass
from pathlib import Path
from src.strategy_system.stocks.stock.components.IncomeStatement import IncomeStatement
from src.strategy_system.stocks.stock.components.Earnings import Earnings, EarningsStatement
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
    earnings: EarningsStatement
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
    def from_alpha_vantage_data(cls, ticker: str, data_base_path: Path = PATH_TO_STOCK_DATA):
        paths = DataPaths.build_paths(ticker, data_base_path)
        income_statement: IncomeStatement = IncomeStatement.from_json_file(
            paths.income_statement_file_path)
        earnings: EarningsStatement = EarningsStatement.from_json_file(
            paths.earnings_file_path)
        balance_sheet: BalanceSheet = BalanceSheet.from_json_file(
            paths.balance_sheet_file_path)
        cash_flow: CashFlow = CashFlow.from_json_file(
            paths.cash_flow_file_path)
        company_overview: CompanyOverview = CompanyOverview.from_json_file(
            paths.company_overview_file_path)

        cls(ticker, income_statement, earnings,
            balance_sheet, cash_flow, company_overview)

    @property
    def graham_number(self):
        GrahamNumberCalculator(self).run()


@dataclass
class DataPaths():
    income_statement_file_path: Path
    earnings_file_path: Path
    balance_sheet_file_path: Path
    cash_flow_file_path: Path
    company_overview_file_path: Path

    @classmethod
    def build_paths(cls, ticker: str, base_path: Path):
        income_statement_file_name = f"{ticker}.IncomeStatement.json"
        earnings_file_name = f"{ticker}.Earnings.json"
        balance_sheet_file_name = f"{ticker}.BalanceSheet.json"
        cash_flow_file_name = f"{ticker}.CashFlow.json"
        company_overview_file_name = f"{ticker}.CompanyOverview.json"

        income_statement_file_path = base_path/income_statement_file_name
        earnings_file_path = base_path/earnings_file_name
        balance_sheet_file_path = base_path/balance_sheet_file_name
        cash_flow_file_path = base_path/cash_flow_file_name
        company_overview_file_path = base_path/company_overview_file_name

        if not income_statement_file_path.exists():
            raise FileNotFoundError(
                f"{income_statement_file_path} does not exist, and cannot be found")
        if not earnings_file_path.exists():
            raise FileNotFoundError(
                f"{earnings_file_path} does not exist, and cannot be found")
        if not balance_sheet_file_path.exists():
            raise FileNotFoundError(
                f"{balance_sheet_file_path} does not exist, and cannot be found")
        if not cash_flow_file_path.exists():
            raise FileNotFoundError(
                f"{cash_flow_file_path} does not exist, and cannot be found")
        if not company_overview_file_path.exists():
            raise FileNotFoundError(
                f"{company_overview_file_path} does not exist, and cannot be found")

        return cls(
            income_statement_file_path=income_statement_file_path,
            earnings_file_path=earnings_file_path,
            balance_sheet_file_path=balance_sheet_file_path,
            cash_flow_file_path=cash_flow_file_path,
            company_overview_file_path=company_overview_file_path
        )
