
# -*- coding: utf-8 -*-

from dataclasses import dataclass
from pathlib import Path
from typing import List, Dict, Union
from src.strategy_system.stocks.components.StockComponent import StockComponent


# -*- coding: utf-8 -*-

from dataclasses import dataclass
from src.strategy_system.stocks.components.StockComponent import StockComponent


@dataclass
class IncomeReport():
    fiscal_date_ending: str
    reported_currency: str
    gross_profit: float
    total_revenue: float
    cost_of_revenue: float
    cost_of_goods_and_services_sold: float
    operating_income: float
    selling_general_and_administrative: float
    research_and_development: float
    operating_expenses: float
    investment_income_net: float
    net_interest_income: float
    interest_income: float
    interest_expense: float
    depreciation: float
    depreciation_and_amortization: float
    income_before_tax: float
    income_tax_expense: float
    interest_and_debt_expense: float
    net_income_from_continuing_operations: float
    comprehensive_income_net_of_tax: float
    ebit: float
    ebitda: float
    net_income: float
    non_interest_income: float
    other_non_operating_income: float

    @classmethod
    def from_dict(cls, data: dict[str, str]) -> 'IncomeReport':
        try:
            depreciation = float(data.get("depreciation", 0))
        except ValueError as e:
            depreciation = 0
        try:
            interest_income = float(data.get("interestIncome", 0))
        except ValueError as e:
            interest_income = 0
        return cls(
            fiscal_date_ending=data.get("fiscalDateEnding", ""),
            reported_currency=data.get("reportedCurrency", ""),
            gross_profit=float(data.get("grossProfit", 0)),
            total_revenue=float(data.get("totalRevenue", 0)),
            cost_of_revenue=float(data.get("costOfRevenue", 0)),
            cost_of_goods_and_services_sold=float(
                data.get("costofGoodsAndServicesSold", 0)),
            operating_income=float(data.get("operatingIncome", 0)),
            selling_general_and_administrative=float(
                data.get("sellingGeneralAndAdministrative", 0)),
            research_and_development=float(
                data.get("researchAndDevelopment", 0)),
            operating_expenses=float(data.get("operatingExpenses", 0)),
            investment_income_net=float(data.get("investmentIncomeNet", 0)),
            net_interest_income=float(data.get("netInterestIncome", 0)),
            interest_income=interest_income,
            interest_expense=float(data.get("interestExpense", 0)),
            depreciation=depreciation,
            depreciation_and_amortization=float(
                data.get("depreciationAndAmortization", 0)),
            income_before_tax=float(data.get("incomeBeforeTax", 0)),
            income_tax_expense=float(data.get("incomeTaxExpense", 0)),
            interest_and_debt_expense=float(
                data.get("interestAndDebtExpense", 0)),
            net_income_from_continuing_operations=float(
                data.get("netIncomeFromContinuingOperations", 0)),
            comprehensive_income_net_of_tax=float(
                data.get("comprehensiveIncomeNetOfTax", 0)),
            ebit=float(
                data.get("ebit", 0)),
            ebitda=float(
                data.get("ebitda", 0)),
            net_income=float(
                data.get("netIncome", 0)),
            non_interest_income=float(data.get("nonInterestIncome", 0)),
            other_non_operating_income=float(
                data.get("otherNonOperatingIncome", 0))
        )


@ dataclass
class IncomeStatement(StockComponent):
    symbol: str
    annual_reports: List[IncomeReport]
    quarterly_reports: List[IncomeReport]

    @ classmethod
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

    @classmethod
    def from_json_file(cls, path: Path):
        return cls.from_dict(cls.load_json_dict(path))
