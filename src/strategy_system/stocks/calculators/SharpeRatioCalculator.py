
#-*- coding: utf-8 -*-

from stocks.calculators.Calculator import Calculator

class SharpeRatioCalculator(Calculator):
    """
    The Sharpe ratio is a financial metric that measures the excess return of an investment per unit of its risk. It was developed by Nobel laureate William F. Sharpe.

    The Sharpe ratio is calculated by subtracting the risk-free rate of return (such as the yield on a government bond) from the average rate of return of the investment, and dividing the result by the standard deviation of the investment's returns. Mathematically, it can be represented as:

    Sharpe ratio = (Rp - Rf) / σp

    where:
    Rp is the average rate of return of the investment
    Rf is the risk-free rate of return
    σp is the standard deviation of the investment's returns

    A higher Sharpe ratio indicates that the investment has generated a higher return for the amount of risk it has taken on. In general, a Sharpe ratio of 1 or higher is considered good, while a Sharpe ratio of less than 1 may indicate that the investment is not generating enough return for the amount of risk it is taking on.

    It's worth noting that the Sharpe ratio has some limitations and assumptions, including the assumption that investment returns follow a normal distribution, and the fact that it only measures risk relative to the risk-free rate and does not account for other types of risk (such as market risk or liquidity risk). Nonetheless, it is a widely used and respected measure of risk-adjusted performance in finance.
    """
    def __init__(self):
        self.Rp = None
        self.Rf = None
        self.sigma_p = None

    def __init__(self, stock_ticker):
        pass

    def run(self, ):
        pass

