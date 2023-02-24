from pathlib import Path
import requests
from typing import Any

import pandas as pd

from src.strategy_system.stocks.alpha_vantage.API import API
import json
API_KEY = "UYOGYE4MI3DF16W2"


class AlphaVantageData():
    def __init__(self) -> None:
        pass

    @classmethod
    def load(cls, data: dict[str, str]):
        data_class = cls()
        data_class.__dict__ = data
        return data_class


class AlphaVantageClient():

    class IncomeStatement(API):

        @staticmethod
        def get_json_data(symbol: str) -> dict[str, str]:
            url = f'https://www.alphavantage.co/query?function=INCOME_STATEMENT&symbol={symbol}&apikey={API_KEY}'
            r = requests.get(url)
            data = r.json()
            return data

        @classmethod
        def print_json(cls, symbol: str):
            data = cls.get_json_data(symbol)
            print(data)

        @classmethod
        def json_file(cls, symbol: str, path: Path):
            data = cls.get_json_data(symbol)

            with open(path/f"{symbol}.IncomeStatement.json", "w") as fp:
                json.dump(data, fp, indent=4)

    class BalanceSheet(API):

        @staticmethod
        def get_json_data(symbol: str) -> dict[str, str]:
            url = f'https://www.alphavantage.co/query?function=BALANCE_SHEET&symbol={symbol}&apikey={API_KEY}'
            r = requests.get(url)
            data = r.json()
            return data

        @classmethod
        def print_json(cls, symbol: str):
            data = cls.get_json_data(symbol)
            print(data)

    class CashFlow(API):
        @staticmethod
        def print_json(symbol: str):
            url = f'https://www.alphavantage.co/query?function=CASH_FLOW&symbol={symbol}&apikey={API_KEY}'
            r = requests.get(url)
            data = r.json()

            print(data)

    class Earnings(API):
        @staticmethod
        def print_json(symbol: str):
            url = f'https://www.alphavantage.co/query?function=EARNINGS&symbol={symbol}&apikey={API_KEY}'
            r = requests.get(url)
            data = r.json()

            print(data)

    class CompanyOverview(API):
        @staticmethod
        def print_json(symbol: str):
            url = f'https://www.alphavantage.co/query?function=OVERVIEW&symbol={symbol}&apikey={API_KEY}'
            r = requests.get(url)
            data = r.json()
            data_class = AlphaVantageData.load(data)

            print(data)


AVC = AlphaVantageClient
