import minutebar as mb
import numpy as np
from sklearn.linear_model import LinearRegression
from supabase import create_client, Client
import os
from enum import Enum
from enum import IntEnum

from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class SignalTrade(Enum):
    Buy = 'buy'
    Sell = 'sell'
    Hold = 'hold'

def fit(symbol: str, feature: str) -> None:
    supabase_url = os.getenv("SUPABASE_URL")
    supabase_key = os.getenv("SUPABASE_KEY")
    supabase: Client = create_client(supabase_url, supabase_key)

    bars = supabase.table("bar_history") \
                    .select("*") \
                    .filter('symbol','eq',symbol) \
                    .order('timestamp', desc=True) \
                    .limit(10) \
                   .execute()

    if not bars or len(bars) < 10:
        return None
    
    current_price = np.array([bar[feature] for bar in bars])
    pos = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]).reshape(-1, 1)

    model = LinearRegression().fit(pos, current_price)
    slope = float(model.coef_[0])
    intercept = float(model.intercept_)

    model_data = {
        'symbol': symbol,
        'feature': feature,
        'slope': slope,
        'intercept': intercept
    }

    supabase.table("simple_model").insert(model_data).execute()

def predict(symbol: str) -> SignalTrade:
    signal = SignalTrade.Hold
    # measure rolling slope
    fit("AAPL", "current")
    fit("AAPL", "volume")
    fit("SPY", "price")

    supabase_url = os.getenv("SUPABASE_URL")
    supabase_key = os.getenv("SUPABASE_KEY")
    supabase: Client = create_client(supabase_url, supabase_key)

    slope_price = supabase.table("model") \
                    .select("slope") \
                    .filter('symbol','eq',symbol) \
                    .order('timestamp', desc=True) \
                    .limit(1) \
                   .execute()
    slope_volume = supabase.table("model") \
                    .select("volume") \
                    .filter('symbol','eq',symbol) \
                    .order('timestamp', desc=True) \
                    .limit(1) \
                   .execute()

    slope_spy = supabase.table("model") \
                    .select("slope") \
                    .filter('symbol','eq',"SPY") \
                    .order('timestamp', desc=True) \
                    .limit(1) \
                   .execute()

    if slope_price > 0 and slope_volume > 0 and slope_spy > 0:
      return  SignalTrade.Buy
    else:
      return SignalTrade.Sell

      