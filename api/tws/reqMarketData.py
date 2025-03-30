import threading
import time

from ibapi.client import Contract, EClient
from ibapi.ticktype import TickTypeEnum
from ibapi.wrapper import EWrapper


class IbMomoApp(EClient, EWrapper):
    def __init__(self):
        EClient.__init__(self, self)

    def nextValidId(self, orderId):
        self.orderId = orderId

    def nextId(self):
        self.orderId += 1
        return self.orderId

    def error(self, reqId, errorCode, errorString, advanceOrderReject):
        print(
            f"reqId: {reqId}, errorCode: {errorCode}, errorString: {errorString}, orderReject: {advanceOrderReject}"
        )

    def contractDetails(self, reqId, contractDetails):
        # attrs = vars(contractDetails)
        # print("\n".join(f'{name} : {val} for name, val in attrs.items()))
        print(contractDetails.contract)

    def contractDetailsEnd(self, reqId):
        print("End of contract")
        self.disconnect

    def tickPrice(self, reqId, tickType, price, attrib):
        print(
            f"reqId: {reqId}, tickType: {TickTypeEnum.toStr(tickType)} , price: {price}, attrib: {attrib}"
        )

    def tickSize(self, reqId, tickType, size):
        print(
            f"reqId: {reqId}, tickType: {TickTypeEnum.toStr(tickType)} , size: {size} "
        )


app = IbMomoApp()
app.connect("127.0.0.1", 7000, 0)
threading.Thread(target=app.run).start()
time.sleep(1)


aapl = Contract()
aapl.symbol = "AAPL"
aapl.secType = "STK"
aapl.currency = "USD"
aapl.exchange = "SMART"
aapl.primaryExchange = "NASDAQ"

# app.reqContractDetails(app.nextId(), aapl)
for i in range(0, 5):
    print(app.nextId())
