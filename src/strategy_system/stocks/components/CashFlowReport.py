
#-*- coding: utf-8 -*-

from stocks.components.StockComponent import StockComponent

class CashFlowReport(StockComponent):
    def __init__(self):
        self.fiscalDateEnding = None
        self.reportedCurrency = None
        self.operatingCashflow = None
        self.paymentsForOperatingActivities = None
        self.proceedsFromOperatingActivities = None
        self.changeInOperatingLiabilities = None
        self.changeInOperatingAssets = None
        self.depreciationDepletionAndAmortization = None
        self.capitalExpenditures = None
        self.changeInReceivables = None
        self.changeInInventory = None
        self.profitLoss = None
        self.cashflowFromInvestment = None
        self.cashflowFromFinancing = None
        self.proceedsFromRepaymentsOfShortTermDebt = None
        self.paymentsForRepurchaseOfCommonStock = None
        self.paymentsForRepurchaseOfEquity = None
        self.paymentsForRepurchaseOfPreferredStock = None
        self.dividendPayout = None
        self.dividendPayoutCommonStock = None
        self.dividendPayoutPreferredStock = None
        self.proceedsFromIssuanceOfCommonStock = None
        self.proceedsFromIssuanceOfLongTermDebtAndCapitalSecuritiesNet = None
        self.proceedsFromIssuanceOfPreferredStock = None
        self.proceedsFromRepurchaseOfEquity = None
        self.proceedsFromSaleOfTreasuryStock = None
        self.changeInCashAndCashEquivalents = None
        self.changeInExchangeRate = None
        self.netIncome = None

