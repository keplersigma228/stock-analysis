import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.ticker import PercentFormatter

def plot_performance(normalized: pd.DataFrame, path: str, benchmark: str = "SPY") -> None:
    """Plot normalized prices against the benchmark."""
    fig, ax = plt.subplots(figsize=(12, 6.75))
    x = normalized.index
    for ticker in normalized.columns:
        y = normalized[ticker]
        if ticker == benchmark:
            ax.plot(x, y, label=ticker, color="gray", linestyle="--")
        else:
            ax.plot(x, y, label=ticker)
    start_date = normalized.index[0].strftime("%Y-%m-%d")
    end_date = normalized.index[-1].strftime("%Y-%m-%d")
    ax.set_title(f"Growth of 100 invested ({start_date}-{end_date})")
    ax.grid(True, alpha=0.3)
    ax.set_ylabel("Value (start = 100)")
    ax.set_xlabel("")
    ax.axhline(100, color="black", linewidth=0.8, linestyle=":")
    ax.legend(loc="best", frameon=False, fontsize=10)
    ax.spines[["top", "right"]].set_visible(False)

    fig.savefig(path, dpi=150, bbox_inches="tight")
    plt.close(fig)


def plot_risk_return(metrics: pd.DataFrame, start_date: str, end_date: str, path: str, benchmark: str = "SPY") -> None:
        fig, ax = plt.subplots(figsize=(12, 6.75))
        ax.grid(True, alpha=0.3)
        for ticker in metrics.index:
            x = metrics.loc[ticker, "volatility"]
            y = metrics.loc[ticker, "cagr"]
            if ticker == benchmark:
                ax.scatter(x, y, s=50, color="gray", marker="D")
            else:
                ax.scatter(x, y, s=50)
            ax.annotate(ticker, (x, y), textcoords="offset points", xytext=(8, 8))
        ax.set_title(f"Risk vs return ({start_date} - {end_date})")
        ax.set_xlabel("Annual volatility (risk)")
        ax.set_ylabel("CAGR (annual return)")
        ax.xaxis.set_major_formatter(PercentFormatter(1.0))
        ax.yaxis.set_major_formatter(PercentFormatter(1.0))
        ax.spines[["top", "right"]].set_visible(False)
        ax.margins(0.15)

        fig.savefig(path, dpi=150, bbox_inches="tight")
        plt.close(fig)


def plot_drawdown(drawdown: pd.DataFrame, path: str, benchmark: str = "SPY") -> None:
    """Plot drawdown from peak."""
    fig, ax = plt.subplots(figsize=(12, 6.75))
    x = drawdown.index
    for ticker in drawdown.columns:
        y = drawdown[ticker]
        if ticker == benchmark:
            ax.plot(x, y, label=ticker, color="gray", linestyle="--")
        else:
            ax.plot(x, y, label=ticker)
    start_date = drawdown.index[0].strftime("%Y-%m-%d")
    end_date = drawdown.index[-1].strftime("%Y-%m-%d")
    ax.set_title(f"Drawdown from peak ({start_date} - {end_date})")
    ax.grid(True, alpha=0.3)
    ax.set_ylabel("Drawdown")
    ax.set_xlabel("")
    ax.legend(loc="best", frameon=False, fontsize=10)
    ax.yaxis.set_major_formatter(PercentFormatter(1.0))
    ax.spines[["top", "right"]].set_visible(False)
    ax.axhline(0, color="black", linewidth=0.8, linestyle=":")

    fig.savefig(path, dpi=150, bbox_inches="tight")
    plt.close(fig)