

from src.strategy_system.stocks.stock.components.StockComponent import StockComponent


from dataclasses import dataclass


@dataclass
class EarningsReport(StockComponent):
    fiscal_date_ending: str
    reported_date: str
    reported_eps: float
    estimated_eps: float
    surprise_percentage: float
    surprise_dollar: float
    year_ago: float
    year_ago_change_percentage: float

    @classmethod
    def from_dict(cls, data: dict[str, str]) -> 'EarningsReport':
        fiscal_date_ending = data.get('fiscalDateEnding', '')
        reported_date = data.get('reportedDate', '')
        reported_eps = float(data.get('reportedEPS', 0))
        estimated_eps = float(data.get('estimatedEPS', 0))
        surprise_percentage = float(data.get('surprisePercentage', 0))
        surprise_dollar = float(data.get('surpriseDollar', 0))
        year_ago = float(data.get('yearAgo', 0))
        year_ago_change_percentage = float(data.get('yearAgoChangePercent', 0))
        company_id = data.get('symbol', '')
        return cls(fiscal_date_ending, reported_date, reported_eps, estimated_eps, surprise_percentage, surprise_dollar, year_ago, year_ago_change_percentage, company_id)


class Earnings(StockComponent):
    pass
