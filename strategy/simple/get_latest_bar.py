import requests
import os
from supabase import create_client, Client
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def get_latest_bar(feed: str, symbol: str) -> None:
    endpoint = "https://data.alpaca.markets/v2/stocks/bars/latest"
    url = f"{endpoint}?symbols={symbol}&feed={feed}"

    headers = {
        "accept": "application/json",
        "APCA-API-KEY-ID": os.getenv("APCA_API_KEY_ID"),
        "APCA-API-SECRET-KEY": os.getenv("APCA_API_SECRET_KEY")
    }

    response = requests.get(url, headers=headers)
    data = response.json()
    print(data)

    supabase_url = os.getenv("SUPABASE_URL")
    supabase_key = os.getenv("SUPABASE_KEY")
    supabase: Client = create_client(supabase_url, supabase_key)

    supabase.table("minutebar").insert(data).execute()


a = get_latest_bar("AAPL")
# print(a)

