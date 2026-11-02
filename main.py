import argparse
import os
import sys
from datetime import date

from src.data import collect_prices, collect_fundamentals
from src.metrics import compute_metrics, normalize, drawdown_series
from src.plots import plot_performance, plot_risk_return, plot_drawdown


BENCHMARK = "SPY"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
        "Collects price and fundamental data for given tickers "
        "and generates risk/return metrics and charts."
        )
    )
    parser.add_argument(
        "tickers",
        nargs="+",
        help="stock tickers"
    )
    parser.add_argument(
        "--start",
        type=date.fromisoformat,
        default="2020-01-01",
        help="start date, YYYY-MM-DD"
    )
    parser.add_argument(
        "--end",
        type=date.fromisoformat,
        default=None,
        help="end date, YYYY-MM-DD"
    )
    parser.add_argument(
        "--path",
        default="reports",
        help="directory for reports"
    )
    args = parser.parse_args()
    if args.end is not None and args.start >= args.end:
        parser.error("--start must be earlier than --end")
    return args


def main():
    args = parse_args()
    tickers = args.tickers.copy()
    if BENCHMARK not in tickers:
        tickers.append(BENCHMARK)
    prices = collect_prices(tickers, args.start, args.end)
    start_date = prices.index[0].strftime("%Y-%m-%d")
    end_date = prices.index[-1].strftime("%Y-%m-%d")
    fundamentals = collect_fundamentals(args.tickers)
    metrics = compute_metrics(prices)
    normalized = normalize(prices)
    drawdown = drawdown_series(prices)
    path = args.path
    os.makedirs(args.path, exist_ok=True)

    plot_performance(normalized, os.path.join(path, "plot_perfomance.png"), BENCHMARK)
    plot_risk_return(metrics, start_date, end_date, os.path.join(path, "plot_risk_return"), BENCHMARK)
    plot_drawdown(drawdown, os.path.join(path, "plot_drawdown.png"), BENCHMARK)

    metrics.to_csv(os.path.join(path, "metrics.csv"))
    fundamentals.to_csv(os.path.join(path, "fundamentals.csv"))
    prices.to_csv(os.path.join(path, "prices.csv"))

if __name__ == "__main__":
    main()