
#-*- coding: utf-8 -*-

from stocks.components.StockComponent import StockComponent

class BalanceReport(StockComponent):
    def __init__(self):
        self.fiscalDateEnding = None
        self.reportedCurrency = None
        self.totalAssets = None
        self.totalCurrentAssets = None
        self.cashAndCashEquivalentsAtCarryingValue = None
        self.cashAndShortTermInvestments = None
        self.inventory = None
        self.currentNetReceivables = None
        self.totalNonCurrentAssets = None
        self.propertyPlantEquipment = None
        self.accumulatedDepreciationAmortizationPPE = None
        self.intangibleAssets = None
        self.intangibleAssetsExcludingGoodwill = None
        self.goodwill = None
        self.investments = None
        self.longTermInvestments = None
        self.shortTermInvestments = None
        self.otherCurrentAssets = None
        self.otherNonCurrentAssets = None
        self.totalLiabilities = None
        self.totalCurrentLiabilities = None
        self.currentAccountsPayable = None
        self.deferredRevenue = None
        self.currentDebt = None
        self.shortTermDebt = None
        self.totalNonCurrentLiabilities = None
        self.capitalLeaseObligations = None
        self.longTermDebt = None
        self.currentLongTermDebt = None
        self.longTermDebtNoncurrent = None
        self.shortLongTermDebtTotal = None
        self.otherCurrentLiabilities = None
        self.otherNonCurrentLiabilities = None
        self.totalShareholderEquity = None
        self.treasuryStock = None
        self.retainedEarnings = None
        self.commonStock = None
        self.commonStockSharesOutstanding = None

