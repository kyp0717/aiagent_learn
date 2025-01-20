from alpaca_trade_api.rest import REST, TimeFrame
from datetime import datetime
api = REST()

start_time = datetime(2021, 6, 8, 9, 32)
end_time = datetime(2021, 6, 8, 9, 33)
minute_period = TimeFrame.Minute

api.get_bars("AAPL", minute_period, start_time, end_time, adjustment='raw').df