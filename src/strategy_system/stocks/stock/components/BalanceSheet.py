

from dataclasses import dataclass
from src.strategy_system.stocks.stock.components.StockComponent import StockComponent


@dataclass
class BalanceReport(StockComponent):
    fiscal_date_ending: str
    reported_currency: str
    total_assets: float
    total_current_assets: float
    cash_and_cash_equivalents_at_carrying_value: float
    cash_and_short_term_investments: float
    inventory: float
    current_net_receivables: float
    total_non_current_assets: float
    property_plant_equipment: float
    accumulated_depreciation_amortization_ppe: float
    intangible_assets: float
    intangible_assets_excluding_goodwill: float
    goodwill: float
    investments: float
    long_term_investments: float
    short_term_investments: float
    other_current_assets: float
    other_non_current_assets: float
    total_liabilities: float
    total_current_liabilities: float
    current_accounts_payable: float
    deferred_revenue: float
    current_debt: float
    short_term_debt: float
    total_non_current_liabilities: float
    capital_lease_obligations: float
    long_term_debt: float
    current_long_term_debt: float
    long_term_debt_noncurrent: float
    short_long_term_debt_total: float
    other_current_liabilities: float
    other_non_current_liabilities: float
    total_shareholder_equity: float
    treasury_stock: float
    retained_earnings: float
    common_stock: float
    common_stock_shares_outstanding: float
