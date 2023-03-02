

class StocksInUse:
    def __init__(self):
        self.stock_tickers: list[str]
        self.data_cache = None
        self.stocks = None

    def cache_all(self, ):
        pass

    def load_stock(self, ticker: str):
        pass

    def is_stock_loaded(self, ticker: str):
        pass

    def get_stock(self, ticker: str):
        pass
