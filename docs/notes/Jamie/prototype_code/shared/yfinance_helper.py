import yfinance as yf  # type:ignore

msft = yf.Ticker("MSFT")
pass

print(msft.balance_sheet)

data = msft.history(period="1mo")  # type:ignore

pass
