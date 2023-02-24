
# -*- coding: utf-8 -*-
from abc import ABC
from pathlib import Path


class API(ABC):

    @classmethod
    def print_json(cls, symbol: str):
        pass

    @classmethod
    def json_file(cls, symbol: str, path: Path):
        pass

    @classmethod
    def to_dict(symbol: str):
        pass
