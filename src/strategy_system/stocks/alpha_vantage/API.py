
# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod
from pathlib import Path


class API(ABC):

    @abstractmethod
    @staticmethod
    def print_json(symbol: str):
        pass

    @abstractmethod
    @staticmethod
    def to_json_file(symbol: str, path: Path):
        pass

    @abstractmethod
    @staticmethod
    def to_dict(symbol: str):
        pass

    @abstractmethod
    @staticmethod
    def from_local_file(symbol: str, cache_path: Path):
        pass
