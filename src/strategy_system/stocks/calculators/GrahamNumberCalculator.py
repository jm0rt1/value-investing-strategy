# type:ignore
from __future__ import annotations
# from stocks.calculators.Calculator import Calculator

from src.strategy_system.stocks.stock.Stock import Stock


class GrahamNumberCalculator():

    def __init__(self, stock: Stock):
        self.stock = stock

    def run(self, ) -> float:
        self.stock.company_overview.eps

    @staticmethod
    def calculate(eps: float, book_value: float):
        pass
