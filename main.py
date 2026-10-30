import sys


def parse_args():
    parser = argparse.ArgumentParser(description=description="Collects price and fundamental data for given tickers and generates risk/return metrics and charts.")
    parser.add_argument("tickers", narge="+", help="stock tickers")
    parser.add_argument("--start", default="2020-01-01", help="start date, YYYY-MM-DD")
    parser.add_argument("--end", default=None, help="end date, YYYY-MM-DD")
    
     