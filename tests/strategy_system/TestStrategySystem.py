import unittest

from src.strategy_system.StrategySystem import StrategySystem


class TestStrategySystem(unittest.TestCase):

    def test_get_stock(self):
        StrategySystem.get_stock("ABC")

    def test_all_stocks(self):
        for ticker in StrategySystem.get_available_stocks():
            StrategySystem.get_stock(ticker)
