import pandas as pd


TRADING_DAYS = 252


def daily_returns(prices: pd.DataFrame):
    """Daily percentage returns for each ticker."""
    return prices.pct_change().dropna()


def cagr(prices):
    """CAGR for each ticker."""
    initial_price = prices.iloc[0]
    last_price = prices.iloc[-1]
    n_days = len(prices)
    return (last_price / initial_price) ** (TRADING_DAYS/n_days) - 1
    

def annual_volatility(returns):
    """Annual volatility for each ticker."""
    standard_deviation = returns.std()
    return standard_deviation * (TRADING_DAYS ** 0.5)


def drawdown_series(prices: pd.DataFrame) -> pd.DataFrame:
    """Drawdawn from the running peak for each day and ticker"""
    return (prices / prices.cummax() - 1)


def max_drawdown(prices: pd.DataFrame) -> pd.DataFrame:
    """Maximum drawdown for each ticker."""
    return drawdown_series(prices).min()


def compute_metrics(prices):
    returns = daily_returns(prices)
    return pd.DataFrame({
        "cagr": cagr(prices),
        "volatility": annual_volatility(returns),
        "max_drawdown": max_drawdown(prices)
    })


def normalize(prices: pd.DataFrame) -> None:
    """Rebase prices so every ticker starts at 100"""
    return prices / prices.iloc[0] * 100




