import unittest
from src.strategy_system.stocks.calculators import GrahamNumberCalculator
from src.strategy_system.stocks.stock.Stock import Stock


class TestGrahamNumberCalculator(unittest.TestCase):

    def test_init(self):
        stock = Stock.from_alpha_vantage_data("AAPL")
        GrahamNumberCalculator(stock)

    def test_calculate(self):
        out = GrahamNumberCalculator.calculate(45, 52)
        self.assertEqual(expected, out)
