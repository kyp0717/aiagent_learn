import sys
import threading
import time

from ibapi.client import EClient, Order, OrderId
from ibapi.wrapper import EWrapper
from loguru import logger

logger.add(sys.stderr, level="TRACE")

port = 7500
bank = {}
position_ref = {}


class TestApp(EClient, EWrapper):
    def __init__(self):
        EClient.__init__(self, self)
        symbol = "NVDA"

    def nextValidId(self, orderId: OrderId):
        logger.info(f"Initial OrderId Created: {orderId}")
        self.orderId = orderId

    def nextId(self):
        self.orderId += 1
        return self.orderId

    def error(self, reqId, errorCode, errorString, advanceOrderReject):
        logger.error(
            f"ReqId: {reqId} --- ErrorCode: {errorCode}, ErrorString: {errorString}"
        )
        logger.error(f"ReqId: {reqId} --- Order Reject: {advanceOrderReject} ")

    def updateAccountValue(self, key, val, currency, accountName):
        if key == "TotalCashBalance" and currency == "BASE":
            bank[key] = float(val)

            # If we drop below $1M, disconnect
            if float(val) < 1000000:
                self.disconnect()

    def position(self, account, contract, position, avgCost):
        position_ref[contract.symbol] = position

    def tickPrice(self, reqId, tickType, price, attrib):
        if "LAST" not in bank[reqId].keys():
            bank[reqId]["LAST"] = price

        bankTick = bank[reqId]["LAST"]
        bankContract = bank[reqId]["contract"]

        order = Order()
        order.tif = "DAY"
        order.totalQuantity = 5
        order.orderType = "MKT"

        # If the new price is more than 5% higher than our previous price point.
        if (bankTick * 1.05) < price:
            order.action = "BUY"
            app.placeOrder(app.nextId(), bankContract, order)
        # If the new price is less than 6% of our previous price point
        elif (bankTick * 0.94) > price and position_ref[bankContract.symbol] >= 5:
            order.action = "SELL"
            app.placeOrder(app.nextId(), bankContract, order)

        bank[reqId]["LAST"] = price

    def openOrder(self, orderId, contract, order, orderState):
        logger.info(
            f"{orderState.status}: ID:{orderId} || {order.action} {order.totalQuantity} {contract.symbol}"
        )
        if orderState.status == "Rejected":
            ## TODO
            pass

    def execDetails(self, reqId, contract, execution):
        print(
            f"Execution Details: ID:{execution.orderId} || {execution.side} {execution.shares} {contract.symbol} @ {execution.time}"
        )


logger.info("Creating the first app")
app = TestApp()
app.connect("localhost", port, 1005)
threading.Thread(target=app.run).start()
time.sleep(1)

app.reqAccountUpdates(True, "")
app.reqPositions()
