import requests
import os
from supabase import create_client, Client
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def paca_get_latest_bar(feed: str, symbol: str) -> None:
    endpoint = "https://data.alpaca.markets/v2/stocks/bars/latest"
    url = f"{endpoint}?symbols={symbol}&feed={feed}"

    headers = {
        "accept": "application/json",
        "APCA-API-KEY-ID": os.getenv("APCA_API_KEY_ID"),
        "APCA-API-SECRET-KEY": os.getenv("APCA_API_SECRET_KEY")
    }

    response = requests.get(url, headers=headers)
    data = response.json()
    bar = data['bars'][symbol]
    print(bar)

    bar = {
    'symbol': symbol,
    'current': bar['c'],
    'high': bar['h'],
    'low': bar['l'],
    'volume': bar['v'],
    'vw': bar['vw'],
    'open': bar['o'],
    'n':bar['n'],
    'timestamp': bar['t']
    }

    supabase_url = os.getenv("SUPABASE_URL")
    supabase_key = os.getenv("SUPABASE_KEY")
    supabase: Client = create_client(supabase_url, supabase_key)

    supabase.table("bar_realtime").insert(bar).execute()


def paca_get_history_bar(feed: str, symbol: str) -> None:
    endpoint = "https://data.alpaca.markets/v2/stocks/bars"
    url =f"{endpoint}?symbols={symbol}&timeframe=1Min&start=2024-01-03T00%3A00%3A00Z&end=2024-01-04T00%3A00%3A00Z&limit=50&adjustment=raw&feed=sip&sort=asc"

    headers = {
        "accept": "application/json",
        "APCA-API-KEY-ID": os.getenv("APCA_API_KEY_ID"),
        "APCA-API-SECRET-KEY": os.getenv("APCA_API_SECRET_KEY")
    }

    response = requests.get(url, headers=headers)
    data = response.json()

    bars = data['bars'][symbol]
    supabase_url = os.getenv("SUPABASE_URL")
    supabase_key = os.getenv("SUPABASE_KEY")
    supabase: Client = create_client(supabase_url, supabase_key)

    for i in bars:
        bar = {
        'symbol': symbol,
        'current': i['c'],
        'high': i['h'],
        'low': i['l'],
        'volume': i['v'],
        'vw': i['vw'],
        'open': i['o'],
        'n':i['n'],
        'timestamp': i['t']
        }

        supabase.table("bar_history").insert(bar).execute()

def pg_fetch_bars(symbol: str):
    supabase_url = os.getenv("SUPABASE_URL")
    supabase_key = os.getenv("SUPABASE_KEY")
    supabase: Client = create_client(supabase_url, supabase_key)

    response = supabase.table("bar_history") \
                    .select("*") \
                    .filter('symbol','eq',symbol) \
                    .order('timestamp', desc=True) \
                    .limit(10) \
                   .execute()
    return response.data




