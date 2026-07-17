import requests
import pandas as pd
from datetime import datetime

def get_current_and_weekly_open(symbol):
    kline_url = "https://api.binance.com/api/v3/klines"
    kline_params = {"symbol": symbol, "interval": "1w", "limit": 1}
    kline_res = requests.get(kline_url, params=kline_params)
    if kline_res.status_code != 200:
        raise Exception(f"{symbol} weekly open price could not be fetched.")
    weekly_open_price = float(kline_res.json()[0][1])
    
    ticker_url = "https://api.binance.com/api/v3/ticker/price"
    ticker_params = {"symbol": symbol}
    ticker_res = requests.get(ticker_url, params=ticker_params)
    if ticker_res.status_code != 200:
        raise Exception(f"{symbol} current price could not be fetched.")
    current_price = float(ticker_res.json()["price"])
    
    return weekly_open_price, current_price

def get_decimal_format(price):
    if price < 0.1: return ".6f"
    elif price < 1.0: return ".4f"
    elif price < 100.0: return ".3f"
    else: return ".2f"

def main():
    symbols = ["BTCUSDT", "ETHUSDT", "SOLUSDT", "DOGEUSDT", "ZECUSDT", "XRPUSDT"]
    print(f"Analysis Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("-" * 75)
    print(f"{'Symbol':<10} | {'Weekly Open ($)':<20} | {'Current Price ($)':<15} | {'Weekly Return':<15}")
    print("-" * 75)
    
    for sym in symbols:
        try:
            open_price, current_price = get_current_and_weekly_open(sym)
            weekly_return = ((current_price - open_price) / open_price) * 100
            direction = "🔺" if weekly_return >= 0 else "🔻"
            fmt = get_decimal_format(open_price)
            print(f"{sym:<10} | {open_price:<20{fmt}} | {current_price:<15{fmt}} | {direction} {weekly_return:+.2f}%")
        except Exception as e:
            print(f"{sym:<10} | Error: {e}")

if __name__ == "__main__":
    main()