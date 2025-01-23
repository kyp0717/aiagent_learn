import numpy as np
from sklearn.linear_model import LinearRegression
from supabase import create_client, Client
import os
from enum import Enum
from enum import IntEnum
import logging
import sys
import minutebarxx as mb
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
# Configure logging to console and file
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(),
        # logging.FileHandler("algo.log")
    ]
)

class SignalTrade(Enum):
    Buy = 'buy'
    Sell = 'sell'
    Hold = 'hold'



def fit(symbol: str, feature: str) -> float:
    ## load bar data to postgres
    logging.info(f"Fit: fetching bar data and load to supabase ...")
    bars = mb.paca_get_bars(feed="iex",symbol=symbol)
  
    logging.info(f"Fit: calc slope of price and volume for {symbol}")
    feat = np.array([bar[feature] for bar in bars])
    pos = np.array([1, 2, 3, 4, 5, 6]).reshape(-1, 1)

    model = LinearRegression().fit(pos, feat)
    slope = float(model.coef_[0])
    # intercept = float(model.intercept_)
    return slope



def predict(symbol: str) -> SignalTrade:
    # signal = SignalTrade.Hold
    # measure rolling slope

    logging.info(f"Model: fitting ...")
    price_indicator =fit(symbol, "current")
    volume_indicator = fit(symbol, "volume")
    benchmark_sp500 = fit("SPY", "current")
    
    logging.info(f"Model: generate trade signal ...")
    if price_indicator > 0 and \
       volume_indicator > 0 and \
       benchmark_sp500 > 0:
      return  SignalTrade.Buy
    else:
      return SignalTrade.Sell

      