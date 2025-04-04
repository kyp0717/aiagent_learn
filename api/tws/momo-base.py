
from ibapi.client import EClient
from ibapi.wrapper import EWrapper
import datetime
import time
import threading

port = 7500
host = 127.0.0.1

bank = {}
position = {}

class Momo(EWrapper,EClient):
    def __init__(self):
        EClient.__init__(self,self)

    def nextValidId(self, orderId):
        self.orderId = orderId

