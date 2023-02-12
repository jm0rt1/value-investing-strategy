# API Key:
# UYOGYE4MI3DF16W2
import requests
from typing import Any
API_KEY = "UYOGYE4MI3DF16W2"


class AlphaVantageData():
    def __init__(self) -> None:
        pass

    @classmethod
    def load(cls, data):
        data_class = cls()
        data_class.__dict__ = data
        return data_class


class AlphaVantageClient():
    @staticmethod
    def get_income_statement(symbol: str):
        # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
        url = f'https://www.alphavantage.co/query?function=INCOME_STATEMENT&symbol={symbol}&apikey={API_KEY}'
        r = requests.get(url)
        data = r.json()

        print(data)

    class FinancialOverview():
        @staticmethod
        def print_json(symbol: str):
            url = f'https://www.alphavantage.co/query?function=OVERVIEW&symbol={symbol}&apikey={API_KEY}'
            r = requests.get(url)
            data = r.json()
            data_class = AlphaVantageData.load(data)

            print(data)

        @staticmethod
        def


AlphaVantageClient.FinancialOverview.print_json("AAPL")
