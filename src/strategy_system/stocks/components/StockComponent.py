
# -*- coding: utf-8 -*-

from pathlib import Path

from abc import ABC


class StockComponent(ABC):
    def __init__(self):
        pass

    def from_alpha_vantage_data(self, cls, data):
        pass

    def from_json_file(self, path: Path):
        pass
