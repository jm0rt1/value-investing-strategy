
# -*- coding: utf-8 -*-

from dataclasses import dataclass
from typing import List, Dict, Union
from src.strategy_system.stocks.components.StockComponent import StockComponent
from src.strategy_system.stocks.components.IncomeReport import IncomeReport


@dataclass
class IncomeStatement(StockComponent):
    symbol: str
    annual_reports: List[IncomeReport]
    quarterly_reports: List[IncomeReport]

    @classmethod
    def from_dict(cls, data: Dict[str, Union[str, list[dict[str, str]]]]) -> 'IncomeStatement':
        annual_reports: list[IncomeReport] = []
        quarterly_reports: list[IncomeReport] = []

        raw_annual_reports: list[dict[str, str]
                                 ] = data.get("annualReports", [])

        raw_qtrly_reports: list[dict[str, str]
                                ] = data.get("quarterlyReports", [])

        if type(raw_annual_reports) is str:
            raise TypeError("Annual reports should not be a string")
        if type(raw_qtrly_reports) is str:
            raise TypeError("Quarterly reports should not be a string")

        for report in raw_annual_reports:
            annual_reports.append(IncomeReport.from_dict(report))
        for report in raw_qtrly_reports:
            quarterly_reports.append(IncomeReport.from_dict(report))

        symbol = data.get("symbol", "")
        if type(symbol) is not str:
            raise TypeError("symbol needs to be a string")
        return cls(
            symbol=symbol,
            annual_reports=annual_reports,
            quarterly_reports=quarterly_reports
        )
