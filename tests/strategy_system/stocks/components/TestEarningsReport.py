from unittest import TestCase
from unittest.mock import patch


class TestEarningsReport(TestCase):

    @patch('my_module.requests.get')
    def test_get_earnings_report(self, mock_get):
        mock_response = {'annualEarnings': [{'fiscalDateEnding': '2020-12-31', 'reportedCurrency': 'USD', 'grossProfit': '123456', 'incomeBeforeTax': '234567', 'incomeTaxExpense': '345678', 'netIncome': '456789', 'researchAndDevelopment': '567890', 'sellingGeneralAndAdmin': '678901', 'operatingIncome': '789012',
                                             'interestExpense': '890123', 'netInterestIncome': '901234', 'ebit': '012345', 'ebitda': '123456', 'basicEPS': '234567', 'dilutedEPS': '345678', 'numberOfSharesBasic': '456789', 'numberOfSharesDiluted': '567890', 'link': 'https://www.sec.gov/Archives/edgar/data/320193/000032019320000096/aapl-20200926.htm'}]}
        mock_get.return_value.json.return_value = mock
