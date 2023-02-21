
#-*- coding: utf-8 -*-

from stocks.components.StockComponent import StockComponent

class EarningsReport(StockComponent):
    def __init__(self):
        self.fiscalDateEnding = None
        self.reportedDate = None
        self.reportedEPS = None
        self.estimatedEPS = None

