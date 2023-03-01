
# -*- coding: utf-8 -*-

from dataclasses import dataclass
from typing import Any
from stocks.components.StockComponent import StockComponent


@dataclass
class IncomeReport(StockComponent):
    fiscal_date_ending: str
    reported_currency: str
    gross_profit: float
    total_revenue: float
    cost_of_revenue: float
    cost_of_goods_and_services_sold: float
    operating_income: float
    selling_general_and_administrative: float
    research_and_development: float
    operating_expense: float
    current_assets: float
    total_assets: float
    total_liabilities: float
    current_cash: float
    current_debt: float
    short_term_debt: float
    long_term_debt: float
    total_cash: float
    total_debt: float
    shareholder_equity: float
    cash_flow: float

    @classmethod
    def from_dict(cls, data: dict[str, str]) -> 'IncomeReport':
        return cls(
            fiscal_date_ending=data.get("fiscalDateEnding", ""),
            reported_currency=data.get("reportedCurrency", ""),
            gross_profit=float(data.get("grossProfit", 0)),
            total_revenue=float(data.get("totalRevenue", 0)),
            cost_of_revenue=float(data.get("costOfRevenue", 0)),
            cost_of_goods_and_services_sold=float(
                data.get("costOfGoodsAndServicesSold", 0)),
            operating_income=float(data.get("operatingIncome", 0)),
            selling_general_and_administrative=float(
                data.get("sellingGeneralAndAdministrative", 0)),
            research_and_development=float(
                data.get("researchAndDevelopment", 0)),
            operating_expense=float(data.get("operatingExpense", 0)),
            current_assets=float(data.get("currentAssets", 0)),
            total_assets=float(data.get("totalAssets", 0)),
            total_liabilities=float(data.get("totalLiabilities", 0)),
            current_cash=float(data.get("currentCash", 0)),
            current_debt=float(data.get("currentDebt", 0)),
            short_term_debt=float(data.get("shortTermDebt", 0)),
            long_term_debt=float(data.get("longTermDebt", 0)),
            total_cash=float(data.get("totalCash", 0)),
            total_debt=float(data.get("totalDebt", 0)),
            shareholder_equity=float(data.get("shareholderEquity", 0)),
            cash_flow=float(data.get("cashflow", 0))
        )
