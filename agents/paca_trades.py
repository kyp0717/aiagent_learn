import datetime
import threading

import alpaca_trade_api as tradeapi
import time
from alpaca_trade_api.rest import TimeFrame
import pandas as pd

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

PACA_KEY = os.getenv('ALPACA_API_KEY')
KEY="PKUMDZ81BB9ZBX7NV8FG"
PACA_SECRET = os.getenv('ALPACA_SECRET_KEY')
SECRET ="7R1ub9iweFPuvUYpgV3x0fVSIbniQkf4Gf9i1loF"
PACA_URL = "https://paper-api.alpaca.markets"


# Initialize the Alpaca API
# api = tradeapi.REST(PACA_KEY, PACA_SECRET, PACA_URL, api_version='v2')
api = tradeapi.REST(KEY, SECRET, PACA_URL, api_version='v2')
def fetch_apple_trades():
    # Define the symbol and time range for the trade data
    symbol = 'AAPL'
    start_date = '2023-01-01'
    end_date = '2023-01-31'

    # Fetch the trade data
    trades = api.get_trades(symbol, start=start_date, end=end_date)

    # Print the trade data
    for trade in trades:
        print(f"Timestamp: {trade.t}, Price: {trade.p}, Size: {trade.s}")

if __name__ == "__main__":
    fetch_apple_trades()
