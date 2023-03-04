

from src.strategy_system.stocks.components.StockComponent import StockComponent


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

    # current_assets: float
    # current_assets = float(data.get("currentAssets", 0)),
    # total_assets: float
    # total_assets = float(data.get("totalAssets", 0)),
    # total_liabilities: float
    # total_liabilities = float(data.get("totalLiabilities", 0)),
    # current_cash: float
    # current_cash = float(data.get("currentCash", 0)),
    # current_debt: float
    # current_debt = float(data.get("currentDebt", 0)),
    # short_term_debt: float
    # short_term_debt = float(data.get("shortTermDebt", 0)),
    # long_term_debt: float
    # long_term_debt = float(data.get("longTermDebt", 0)),
    # total_cash: float
    # total_cash = float(data.get("totalCash", 0)),
    # total_debt: float
    # total_debt = float(data.get("totalDebt", 0)),
    # shareholder_equity: float
    # shareholder_equity = float(data.get("shareholderEquity", 0)),
    # cash_flow: float
    # cash_flow = float(data.get("cashflow", 0)),
    # gross_revenue: float
    # gross_revenue = float(data.get("grossRevenue", 0)),
