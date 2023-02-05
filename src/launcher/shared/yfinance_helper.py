import yfinance as yf

msft = yf.Ticker("MSFT")
pass

print(msft.balance_sheet)

data = msft.history(period="1mo")

pass
