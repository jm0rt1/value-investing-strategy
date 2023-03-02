# API Key:
# UYOGYE4MI3DF16W2
import requests
from typing import Any

import pandas as pd

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

    class IncomeStatement():
        @staticmethod
        def print_json(symbol: str):
            # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
            url = f'https://www.alphavantage.co/query?function=INCOME_STATEMENT&symbol={symbol}&apikey={API_KEY}'
            r = requests.get(url)
            data = r.json()

            print(data)

    class BalanceSheet():
        @staticmethod
        def print_json(symbol: str):
            url = f'https://www.alphavantage.co/query?function=BALANCE_SHEET&symbol={symbol}&apikey={API_KEY}'
            r = requests.get(url)
            data = r.json()

            print(data)

    class CashFlow():
        @staticmethod
        def print_json(symbol: str):
            url = f'https://www.alphavantage.co/query?function=CASH_FLOW&symbol={symbol}&apikey={API_KEY}'
            r = requests.get(url)
            data = r.json()

            print(data)

    class Earnings():
        @staticmethod
        def print_json(symbol: str):
            url = f'https://www.alphavantage.co/query?function=EARNINGS&symbol={symbol}&apikey={API_KEY}'
            r = requests.get(url)
            data = r.json()

            print(data)

    class CompanyOverview():
        @staticmethod
        def print_json(symbol: str):
            url = f'https://www.alphavantage.co/query?function=OVERVIEW&symbol={symbol}&apikey={API_KEY}'
            r = requests.get(url)
            data = r.json()
            data_class = AlphaVantageData.load(data)

            print(data)


AVC = AlphaVantageClient
