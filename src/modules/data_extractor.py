import yfinance as yf

def get_stock_data(ticker, period="max"):
    stock = yf.Ticker(ticker)
    data = stock.history(period=period)
    return data
