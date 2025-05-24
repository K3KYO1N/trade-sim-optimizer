# backend/app/utils.py
import yfinance as yf

def fetch_current_price(symbol: str) -> float:
    data = yf.Ticker(symbol)
    hist = data.history(period="1d")
    if hist.empty:
        raise ValueError("No price data found for symbol")
    return float(round(hist["Close"].iloc[0], 2))