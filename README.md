# Stock Analysis

A command-line tool that downloads market data for a list of stock tickers, computes key risk/return and fundamental metrics, and generates presentation-ready charts — all compared against a market benchmark (S&P 500 via `SPY`).

Built for an investment competition to support a stock-picking pitch with data instead of intuition.

## Features

- **Data collection** — daily adjusted close prices and company fundamentals via [yfinance](https://github.com/ranaroussi/yfinance)
- **Risk & return metrics** — CAGR, annualized volatility, maximum drawdown
- **Fundamentals table** — market cap, P/E, forward P/E, revenue growth, profit margin, debt-to-equity, ROE
- **Charts** — growth vs benchmark, risk vs return, drawdown from peak
- **Benchmark included automatically** — every run is compared against `SPY`
- **CSV export** — all tables can be opened in Excel or Google Sheets

## Example output

<!-- Add a chart here, e.g. copy one PNG to docs/ and uncomment: -->
<!-- ![Growth vs S&P 500](docs/performance.png) -->

## Installation

```bash
git clone git@github.com:keplersigma228/stock-analysis.git
cd stock-analysis
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Usage

```bash
python main.py AAPL MSFT NVDA
```

Options:

| Argument | Default | Description |
|---|---|---|
| `tickers` | — | One or more stock tickers (required) |
| `--start` | `2020-01-01` | Start date, `YYYY-MM-DD` |
| `--end` | today | End date, `YYYY-MM-DD` |
| `--path` | `reports` | Output directory |

Examples:

```bash
python main.py AAPL MSFT --start 2018-01-01
python main.py GLD --start 2010-01-01 --path reports/gold
python main.py --help
```

## Output

All results are saved to the output directory (`reports/` by default):

| File | Content |
|---|---|
| `performance.png` | Growth of 100 invested in each ticker vs the benchmark |
| `risk_return.png` | Annualized volatility vs CAGR for each ticker |
| `drawdown.png` | Drawdown from running peak over time |
| `metrics.csv` | CAGR, volatility and max drawdown per ticker |
| `fundamentals.csv` | Fundamental metrics per company |
| `prices.csv` | Daily adjusted close prices |

## Metrics

With $P_t$ the adjusted close price on day $t$ and $n$ the number of trading days:

- **Daily return:** $r_t = \frac{P_t}{P_{t-1}} - 1$
- **CAGR:** $\left(\frac{P_{\text{last}}}{P_{\text{first}}}\right)^{252/n} - 1$
- **Annualized volatility:** $\text{std}(r_t) \cdot \sqrt{252}$
- **Drawdown:** $\frac{P_t}{\max(P_0, \dots, P_t)} - 1$
- **Max drawdown:** $\min_t \text{Drawdown}_t$

252 is the standard number of trading days in a year. All tickers are compared over their **common** period: if one ticker started trading later, earlier dates are dropped.

## Project structure

```
stock-analysis/
├── src/
│   ├── data.py       # price and fundamentals download
│   ├── metrics.py    # risk/return calculations
│   └── plots.py      # charts
├── main.py           # CLI entry point
└── requirements.txt
```

## Limitations

- Data comes from Yahoo Finance via `yfinance`, which is unofficial and may occasionally be incomplete or rate-limited.
- Fundamentals are a current snapshot, not historical values.
- Past performance does not guarantee future results. This project is for educational purposes and is not investment advice.
