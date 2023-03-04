import unittest
import json
from src.strategy_system.stocks.stock.components.IncomeStatement import IncomeReport


class TestIncomeReport(unittest.TestCase):
    def test_from_file(self):
        with open('sample_income_report.json', 'r') as f:
            data = json.load(f)
        income_report = IncomeReport.from_dict(data)

        self.assertEqual(income_report.fiscal_date_ending, "2021-09-30")
        self.assertEqual(income_report.reported_currency, "USD")
        self.assertEqual(income_report.gross_profit, 123456.78)
        self.assertEqual(income_report.total_revenue, 234567.89)
        self.assertEqual(income_report.cost_of_revenue, 111111.11)
        # Add more assertions for the remaining attributes
