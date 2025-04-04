import threading
import time

from ibapi.client import EClient
from ibapi.wrapper import EWrapper

port = 7500

bank = {}
position = {}


class Momo(EWrapper, EClient):
    def __init__(self):
        EClient.__init__(self, self)

    def nextValidId(self, orderId):
        self.orderId = orderId

    def nextId(self):
        self.orderId += 1
        return self.orderId

    def error(self, reqId, errorCode, errorString, advanceOrderReject):
        message = (
            f"-- ReqId, {reqId} --\n"
            f"ErrorCode: {errorCode}, ErrorString: {errorString} \n"
            f"Order Reject: {advanceOrderReject} \n"
        )

        print(message)


app = Momo()
app.connect("localhost", port, 1005)
threading.Thread(target=app.run).start
time.sleep(1)

# Account Updates set to true enable streaming of changes to account info
# such as position and pnl
app.reqAccountUpdates(True, "")
