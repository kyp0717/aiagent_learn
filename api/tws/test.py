import threading
import time

from ibapi.client import EClient
from ibapi.wrapper import EWrapper


class TestApp(EClient, EWrapper):
    def __init__(self):
        EClient.__init__(self, self)

    def nextValidId(self, orderId):
        self.orderId = orderId

    def nextId(self):
        self.orderId += 1
        return self.orderId


app = TestApp()
app.connect("127.0.0.1", 7500, 0)
threading.Thread(target=app.run).start()
time.sleep(1)

for i in range(0, 5):
    print(app.nextId())
