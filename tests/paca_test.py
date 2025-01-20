from alpaca_trade_api.rest import REST, TimeFrame
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

api = REST()

a=api.get_bars("AAPL", TimeFrame.Hour, "2021-06-08", "2021-06-08", adjustment='raw').df
print(a)