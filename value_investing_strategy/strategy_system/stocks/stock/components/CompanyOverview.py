

from pathlib import Path
from typing import TypeVar, Union
from strategy_system.stocks.stock.components.StockComponent import StockComponent


from dataclasses import dataclass


@dataclass
class CompanyOverview(StockComponent):
    symbol: str
    asset_type: str
    name: str
    description: str
    cik: int
    exchange: str
    currency: str
    country: str
    sector: str
    industry: str
    address: str
    fiscal_year_end: str
    latest_quarter: str
    market_capitalization: float
    ebitda: float
    pe_ratio: float
    peg_ratio: float
    book_value: float
    dividend_per_share: float
    dividend_yield: float
    eps: float
    revenue_per_share_ttm: float
    profit_margin: float
    operating_margin_ttm: float
    return_on_assets_ttm: float
    return_on_equity_ttm: float
    revenue_ttm: float
    gross_profit_ttm: float
    diluted_eps_ttm: float
    quarterly_earnings_growth_yoy: float
    quarterly_revenue_growth_yoy: float
    analyst_target_price: float
    trailing_pe: float
    forward_pe: float
    price_to_sales_ratio: float
    price_to_book_ratio: float
    ev_to_revenue: float
    ev_to_ebitda: float
    beta: float
    fifty_two_week_high: float
    fifty_two_week_low: float
    fifty_day_moving_average: float
    two_hundred_day_moving_average: float
    shares_outstanding: float
    dividend_date: str
    ex_dividend_date: str

    @classmethod
    def from_dict(cls, data: dict[str, str]):
        try:
            ebitda = float(data.get("EBITDA", 0))
        except ValueError as _:
            ebitda = 0

        try:
            ev_to_revenue = float(data.get("EVToRevenue", 0))
        except ValueError as _:
            ev_to_revenue = 0

        try:
            ev_to_ebitda = float(data.get("EVToEBITDA", 0))
        except ValueError as _:
            ev_to_ebitda = 0
        return cls(
            symbol=data.get("Symbol", ""),
            asset_type=data.get("AssetType", ""),
            name=data.get("Name", ""),
            description=data.get("Description", ""),
            cik=int(data.get("CIK", 0)),
            exchange=data.get("Exchange", ""),
            currency=data.get("Currency", ""),
            country=data.get("Country", ""),
            sector=data.get("Sector", ""),
            industry=data.get("Industry", ""),
            address=data.get("Address", ""),
            fiscal_year_end=data.get("FiscalYearEnd", ""),
            latest_quarter=data.get("LatestQuarter", ""),
            market_capitalization=float(data.get("MarketCapitalization", 0)),
            ebitda=ebitda,
            pe_ratio=float(data.get("PERatio", 0)),
            peg_ratio=float(data.get("PEGRatio", 0)),
            book_value=float(data.get("BookValue", 0)),
            dividend_per_share=float(data.get("DividendPerShare", 0)),
            dividend_yield=float(data.get("DividendYield", 0)),
            eps=float(data.get("EPS", 0)),
            revenue_per_share_ttm=float(data.get("RevenuePerShareTTM", 0)),
            profit_margin=float(data.get("ProfitMargin", 0)),
            operating_margin_ttm=float(data.get("OperatingMarginTTM", 0)),
            return_on_assets_ttm=float(data.get("ReturnOnAssetsTTM", 0)),
            return_on_equity_ttm=float(data.get("ReturnOnEquityTTM", 0)),
            revenue_ttm=float(data.get("RevenueTTM", 0)),
            gross_profit_ttm=float(data.get("GrossProfitTTM", 0)),
            diluted_eps_ttm=float(data.get("DilutedEPSTTM", 0)),
            quarterly_earnings_growth_yoy=float(
                data.get("QuarterlyEarningsGrowthYOY", 0)),
            quarterly_revenue_growth_yoy=float(
                data.get("QuarterlyRevenueGrowthYOY", 0)),
            analyst_target_price=float(data.get("AnalystTargetPrice", 0)),
            trailing_pe=float(data.get("TrailingPE", 0)),
            forward_pe=float(data.get("ForwardPE", 0)),
            price_to_sales_ratio=float(data.get("PriceToSalesRatioTTM", 0)),
            price_to_book_ratio=float(data.get("PriceToBookRatio", 0)),
            ev_to_revenue=ev_to_revenue,
            ev_to_ebitda=ev_to_ebitda,
            beta=float(data.get("Beta", 0)),
            fifty_two_week_high=float(data.get("52WeekHigh", 0)),
            fifty_two_week_low=float(data.get("52WeekLow", 0)),
            fifty_day_moving_average=float(data.get("50DayMovingAverage", 0)),
            two_hundred_day_moving_average=float(
                data.get("200DayMovingAverage", 0)),
            shares_outstanding=float(data.get("SharesOutstanding", 0)),
            dividend_date=data.get("DividendDate", ""),
            ex_dividend_date=data.get("ExDividendDate", ""),

        )

    @classmethod
    def from_json_file(cls, path: Path):
        return cls.from_dict(cls.load_json_dict(path))  # type:ignore
