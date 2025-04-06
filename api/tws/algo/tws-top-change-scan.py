import threading
from datetime import date

from ibapi.client import EClient, ScannerSubscription
from ibapi.tag_value import TagValue
from ibapi.wrapper import EWrapper
from ibapi.

port = 7497
global globalDict
globalDict = {}
global clientId
clientId = 1001


# This is the IBAPI primary EClient and Ewrapper class class TestApp (EClient, EWrapper):
class TestApp(EWrapper, EClient):
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

    # Returned Market Scanner information (One rank at a time)
    def scannerData(
        self,
        reqId: int,
        rank: int,
        contractDetails: ContractDetails,
        distance: str,
        benchmark: str,
        projection: str,
        legsStr: str,
    ):
        global globalDict
        globalDict[rank] = [
            contractDetails.contract,
            "BID",
            "ASK",
            "LAST",
            "Today",
            "Yesterday",
            "today_CHANGE%",
            "prior_CHANGE%",
            "today_CHANG",
        ]

    # End of market scanner
    def scannerDataEnd(self, reqId: int):
        # Cancel lingering market scanner
        self.cancelScannerSubscription(reqId)
        # Request market data for all of our scanner values.
        for rank in globalDict:
            x = threading.Thread(
                target=self.reqMktData(
                    reqId=rank,
                    contract=globalDict[rank][0],
                    genericTicklist="",
                    snapshot=True,
                    regulatorySnapshot=False,
                )
            )
            x.start()

    # Returned market data
    def tickPrice(
        self, reqId: TickerId, tickType: TickType, price: float, attrib: TickAttrib
    ):
        global globalDict
        for ind, value in enumerate(globalDict[reqId]):
            if TickTypeEnum.to_str(tickType) == value:
                globalDict[reqId][ind] = price


def run_loop(app_obj: TestApp):
    print("Run Loop")
    app_obj.run()


# This is an introduction to start using threads and combining requests with one another class startInvesting():
class startInvesting:
    # Normalize Date Values
    def dateCleanUp():
        badDate = date.today().____str___().split("-")
        goodDate = badDate[0] + badDate[1] + badDate[2]
        return goodDate

    # Create the market scanner
    def buildScanner():
        global clientId
        # create all historical data requests def buildHistorical():
        app = TestApp()
        app.connect("127.0.0.1", port, clientId)
        sub = ScannerSubscription()
        sub.instrument = "STK"
        sub.locationCode = "STK.US.MAJOR"
        sub.scanCode = "TOP_PERC_GAIN"

        scan_options = []
        filter_options = [
            TagValue("volumeAbove", "10000"),
            TagValue("marketBelow1e6", "1000"),
            TagValue("priceAbove", "1"),
        ]


def main():
    startInvesting.buildScanner()
    startInvesting.printScanner()
    startInvesting.buildHistorical()
    startInvesting.calcChange()
    startInvesting.printTopDif()
    startInvesting.bestBuys()


if _name_ == "__main__":
    main()
    I
