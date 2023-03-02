
# -*- coding: utf-8 -*-

from src.strategy_system.stocks.components.StockComponent import StockComponent
from src.strategy_system.stocks.components.StockComponent import StockComponent


from dataclasses import dataclass


@dataclass
class CompanyOverview(StockComponent):
    symbol: str
    asset_type: str
    name: str
    description: str
    exchange: str
    currency: str
    country: str
    sector: str
    industry: str
    address: str
    full_time_employees: int
    fiscal_year_end: str
    latest_quarter: str
    market_capitalization: float
    ebitda: float
    pe_ratio: float
    peg_ratio: float
    eps: float
    revenue_per_share: float
    dividend_yield: float
    dividend_per_share: float
    dividend_pay_date: str
    dividend_ex_date: str
    last_split_factor: str
    last_split_date: str
    beta: float
    fifty_two_week_high: float
    fifty_two_week_high_date: str
    fifty_two_week_low: float
    fifty_two_week_low_date: str
    shares_outstanding: float
    book_value_per_share: float
    operating_cash_flow: float
    levered_free_cash_flow: float
    beta_three_year: float
    market_status: str
    forward_pe_ratio: float
    price_to_sales_ratio: float
    price_to_book_ratio: float
    earnings_per_share: float
    revenue: float
    gross_profit: float
    diluted_eps: float
    quarterly_earnings_growth_yoy: float
    quarterly_revenue_growth_yoy: float
    analyst_target_price: float
    trailing_pe_ratio: float

    @classmethod
    def from_dict(cls, data: dict[str, str]):
        return cls(
            symbol=data.get('Symbol', ''),
            asset_type=data.get('AssetType', ''),
            name=data.get('Name', ''),
            description=data.get('Description', ''),
            exchange=data.get('Exchange', ''),
            currency=data.get('Currency', ''),
            country=data.get('Country', ''),
            sector=data.get('Sector', ''),
            industry=data.get('Industry', ''),
            address=data.get('Address', ''),
            full_time_employees=int(data.get('FullTimeEmployees', 0)),
            fiscal_year_end=data.get('FiscalYearEnd', ''),
            latest_quarter=data.get('LatestQuarter', ''),
            market_capitalization=float(data.get('MarketCapitalization', 0)),
            ebitda=float(data.get('EBITDA', 0)),
            pe_ratio=float(data.get('PERatio', 0)),
            peg_ratio=float(data.get('PEGRatio', 0)),
            eps=float(data.get('EPS', 0)),
            revenue_per_share=float(data.get('RevenuePerShare', 0)),
            dividend_yield=float(data.get('DividendYield', 0)),
            dividend_per_share=float(data.get('DividendPerShare', 0)),
            dividend_pay_date=data.get('DividendDate', ''),
            dividend_ex_date=data.get('ExDividendDate', ''),
            last_split_factor=data.get('LastSplitFactor', ''),
            last_split_date=data.get('LastSplitDate', ''),
            beta=float(data.get('Beta', 0)),
            fifty_two_week_high=float(data.get('52WeekHigh', 0)),
            fifty_two_week_high_date=data.get('52WeekHighDate', ''),
            fifty_two_week_low=float(data.get('52WeekLow', 0)),
            fifty_two_week_low_date=data.get('52WeekLowDate', ''),
            shares_outstanding=float(data.get('SharesOutstanding', 0)),
            book_value_per_share=float(data.get('BookValue', 0)),
            operating_cash_flow=float(data.get('OperatingCashflow', 0)),
            levered_free_cash_flow=float(data.get('FreeCashflow', 0)),
            beta_three_year=float(data.get('Beta3Y', 0)),
            market_status=data.get('MarketStatus', ''),
            forward_pe_ratio=float(data.get('ForwardPE', 0)),
            price_to_sales_ratio=float(data.get('PriceToSalesRatioTTM', 0)),
            price_to_book_ratio=float(data.get('PriceToBookRatio', 0)),
            earnings_per_share=float(data.get('TrailingEps', 0)),
            revenue=float(data.get('RevenueTTM', 0)),
            gross_profit=float(data.get('GrossProfitTTM', 0)),
            diluted_eps=float(data.get('DilutedEPSTTM', 0)),
            quarterly_earnings_growth_yoy=float(
                data.get('QuarterlyEarningsGrowthYOY', 0)),
            quarterly_revenue_growth_yoy=float(
                data.get('QuarterlyRevenueGrowthYOY', 0)),
            analyst_target_price=float(data.get('AnalystTargetPrice', 0)),
            trailing_pe_ratio=float(data.get('TrailingPE', 0))
        )
