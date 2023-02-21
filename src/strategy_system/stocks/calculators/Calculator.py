
# -*- coding: utf-8 -*-
from src.strategy_system.stocks.stock.Stock import Stock


class Calculator:
    def __init__(self, stock_ticker: str, stock_data: Stock):
        self.stock_ticker: str = stock_ticker
        self.stock_data = None

    def run(self, ):
        pass
