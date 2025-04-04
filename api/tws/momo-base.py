import threading
import time

from ibapi.client import EClient, ScannerSubscription
from ibapi.tag_value import TagValue
from ibapi.wrapper import EWrapper

port = 7500

bank = {}
position_ref = {}


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

    def updateAccountValue(self, key, val, currency, accountName):
        if key == "TotalCashBalance" and currency == "BASE":
            bank[key] = float(val)

        # if acct drop below $100k disconnect
        if float(val) < 100000:
            self.disconnect

    def position(self, account, contract, position, avgCost):
        position_ref[contract.symbol] = position

    def scannerData(
        self, reqId, rank, contractDetails, distance, benchmark, projection, legsStr
    ):
        if rank < 5:
            rankId = rank + reqId
            bank[rankId] = {"contract": contractDetails.contrac}

    def scannerDataEnd(self, reqId):
        pass

    def tickPrice(self, reqId, ticeType, price, attrib):
        pass

    def openOrder(self, orderId, contract, order, orderState):
        pass

    def execDetails(self, reqId, contract, execution):
        pass


app = Momo()
app.connect("localhost", port, 1005)
threading.Thread(target=app.run).start
time.sleep(1)

# Account Updates set to true enable streaming of changes to account info
# such as position and pnl
app.reqAccountUpdates(True, "")
app.reqPositions()

scanner = ScannerSubscription()
scanner.instrument = "STK"
scanner.locationCode = "STK.US.MAJOR"
scanner.scanCode = "MOST_ACTIVE"
scan_options = []
filter_options = [TagValue("avgVolumeAbove", "1000000"), TagValue("priceAbove", "10")]
