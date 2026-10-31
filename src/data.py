import yfinance as yf
import pandas as pd


def collect_prices(tickers: list[str], start: str, end: str | None = None) -> pd.DataFrame:
    prices = yf.download(tickers, start=start, end=end)
    return prices["Close"].dropna()


def collect_fundamentals(tickers: list[str]):
    rows = []
    for ticker in tickers:
        info = yf.Ticker(ticker).info
        rows.append({
            "ticker": ticker,
            "sector": info.get("sector"),
            "market_cap": info.get("marketCap"),
            "pe": info.get("trailingPE"),
            "forward_pe": info.get("forwardPE"),
            "revenue_growth": info.get("revenueGrowth"),
            "profit_margin": info.get("profitMargins"),
            "debt_to_equity": info.get("debtToEquity"),
            "roe": info.get("returnOnEquity")
        })
    return pd.DataFrame(rows).set_index("ticker")