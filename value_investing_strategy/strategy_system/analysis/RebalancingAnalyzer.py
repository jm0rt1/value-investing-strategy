
# -*- coding: utf-8 -*-

from strategy_system.analysis.Analyzer import Analyzer
from strategy_system.settings.RebalancingAnalyzerSettings import RebalancingAnalyzerSettings


class RebalancingAnalyzer(Analyzer):

    def __init__(self, settings: RebalancingAnalyzerSettings):
        self.uid = None

    def save(self, ):
        pass
