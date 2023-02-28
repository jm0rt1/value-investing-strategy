from pathlib import Path
import unittest
from src.strategy_system.stocks.alpha_vantage.AlphaVantageClient import AlphaVantageClient


class TestIncomeStatement(unittest.TestCase):
    TEST_FILES_PATH = Path(
        "./tests/test_files/outputs/strategy_system/stocks/alpha_vantage/IncomeStatement")
    TEST_FILES_PATH.mkdir(exist_ok=True, parents=True)

    def test_to_file(self):
        AlphaVantageClient.IncomeStatement.to_json_file(
            "AAPL", self.TEST_FILES_PATH)


class TestBalanceSheet(unittest.TestCase):
    TEST_FILES_PATH = Path(
        "./tests/test_files/outputs/strategy_system/stocks/alpha_vantage/BalanceSheet")
    TEST_FILES_PATH.mkdir(exist_ok=True, parents=True)

    def test_to_file(self):
        AlphaVantageClient.BalanceSheet.to_json_file(
            "AAPL", self.TEST_FILES_PATH)
