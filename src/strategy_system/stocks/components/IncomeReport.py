
#-*- coding: utf-8 -*-

from stocks.components.StockComponent import StockComponent

class IncomeReport(StockComponent):
    def __init__(self):
        self.fiscalDateEnding = None
        self.reportedCurrency = None
        self.grossProfit = None
        self.totalRevenue = None
        self.costOfRevenue = None
        self.costofGoodsAndServicesSold = None
        self.operatingIncome = None
        self.sellingGeneralAndAdministrative = None
        self.researchAndDevelopment = None
        self.operatingExpenses = None
        self.investmentIncomeNet = None
        self.netInterestIncome = None
        self.interestIncome = None
        self.interestExpense = None
        self.nonInterestIncome = None
        self.otherNonOperatingIncome = None
        self.depreciation = None
        self.depreciationAndAmortization = None
        self.incomeBeforeTax = None
        self.incomeTaxExpense = None
        self.interestAndDebtExpense = None
        self.netIncomeFromContinuingOperations = None
        self.comprehensiveIncomeNetOfTax = None
        self.ebit = None
        self.ebitda = None
        self.netIncome = None

