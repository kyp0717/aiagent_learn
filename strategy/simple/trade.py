import model as mod
from enum import Enum
from enum import IntEnum

class PacaPosition(Enum):
    Open = 'open'
    Close = 'close'
    Nonexist = 'nonexist'


def get_position(symbol: str) -> PacaPosition:
    pass


def run_simple_model(symbol: str):
    while True:
        # check current position of stock
        p = get_position(symbol)
        if p==PacaPosition.Close:
            print("position is closed")
            break
        
        signal = mod.predict(symbol)

        if signal == mod.SignalTrade.Buy:
            if p==PacaPosition.Nonexist:
                paca.buy(symbol)
            elif p==PacaPosition.Open:
                pass
        elif signal == mod.SignalTrade.Sell:
            paca.sell(symbol)

    print("Simple Algo has closed")
