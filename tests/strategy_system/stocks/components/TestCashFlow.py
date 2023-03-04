from unittest import TestCase
from unittest.mock import patch
from src.strategy_system.stocks.stock.components.CashFlowReport import CashFlowReport


class TestCashFlowReport(TestCase):

    @patch('my_module.requests.get')
    def test_get_cashflow_report(self, mock_get):
        mock_response = {'annualReports': [{'fiscalDateEnding': '2020-12-31', 'reportedCurrency': 'USD', 'operatingCashflow': '123456', 'changeInOperatingAssets': '234567', 'capitalExpenditures': '345678', 'investments': '456789', 'dividendsPaid': '567890',
                                            'netCashFromFinancingActivities': '678901', 'changeInCashAndCashEquivalents': '789012', 'effectOfExchangeRateChanges': '890123', 'netIncome': '901234', 'changeInInventory': '012345', 'changeInAccountReceivables': '123456', 'capitalLeaseObligations': '234567', 'freeCashFlow': '345678'}]}
        mock_get.return_value.json.return_value = mock_response
        report = CashFlowReport.from_dict(mock_response['annualReports'][0])

        self.assertEqual(report.fiscal_date_ending, '2020-12-31')
        self.assertEqual(report.reported_currency, 'USD')
        self.assertEqual(report.operating_cashflow, 123456)
        self.assertEqual(report.change_in_operating_assets, 234567)
        self.assertEqual(report.capital_expenditures, 345678)
        self.assertEqual(report.investments, 456789)
        self.assertEqual(report.dividends_paid, 567890)
        self.assertEqual(report.net_cash_from_financing_activities, 678901)
        self.assertEqual(report.change_in_cash_and_cash_equivalents, 789012)
        self.assertEqual(report.effect_of_exchange_rate_changes, 890123)
        self.assertEqual(report.net_income, 901234)
        self.assertEqual(report.change_in_inventory, 12345)
        self.assertEqual(report.change_in_account_receivables, 123456)
        self.assertEqual(report.capital_lease_obligations, 234567)
        self.assertEqual(report.free_cash_flow, 345678)
