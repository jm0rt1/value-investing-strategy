

import abc

from src.strategy_system.analysis.QFAnalyzer import QFAnalyzer


class StrategyInterface(abc.ABC):
    def __init__(self):
        pass

    @abc.abstractmethod
    def run(self, ):
        pass

    @abc.abstractmethod
    def initialize(self, ):

        pass

    @abc.abstractmethod
    def reset(self, ):
        """
        reset the system to defaults
        """
        pass

    @abc.abstractmethod
    def calculate_graham_number(self, ticker: str):
        """
        - load stock object via cache manager
        - return graham number calculation (a property of the stock)

        Args:
            ticker (str): ticker to calculate graham number on
        """

        pass

    @abc.abstractmethod
    def calculate_book_value_dividend_projections_valuation(self, ticker: str):
        """
        - load stock object via cache manager
        - return book value/dividend projection valuation calculation (a property of the stock)

        Args:
            ticker (str): ticker to calculate book value/dividend projection valuation on
        """
        pass

    @abc.abstractmethod
    def compare_qfa(self, tickers: str):
        pass

    @abc.abstractmethod
    def save_qfa(self, analysis_to_save: QFAnalyzer):
        pass

    @abc.abstractmethod
    def calculate_discounted_cash_flow_valuation(self, ticker: str):
        pass

    @abc.abstractmethod
    def calculate_asset_based_valuation(self, ticker: str):
        pass

    @abc.abstractmethod
    def calculator_financial_metric_analysis(self, ticker: str):
        pass

    @abc.abstractmethod
    def calculate_financial_metric_analysis_valuation(self, ticker: str):
        pass

    @abc.abstractmethod
    def generate_qf_analysis(self, ):
        pass

    @abc.abstractmethod
    def generate_rebalancing_analysis(self, ):
        pass

    @abc.abstractmethod
    def add_rebalancing_dataflow(self, analyzer):
        pass

    @abc.abstractmethod
    def add_qfa_dataflow(self, analyzer):
        pass

    @abc.abstractmethod
    def run_rebalance(self, uid):
        pass

    @abc.abstractmethod
    def run_qfa(self, uid):
        pass

    @abc.abstractmethod
    def get_settings(self, ):
        pass

    @abc.abstractmethod
    def compare_stocks(self, tickers):
        pass
