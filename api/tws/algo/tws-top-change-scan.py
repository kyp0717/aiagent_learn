from datetime import date

from ibapi.client import EClient
from ibapi.tag_value import TagValue
from ibapi.wrapper import EWrapper

port = 7497
global globalDict
globalDict = {}
global clientId
clientId = 1001


# This is the IBAPI primary EClient and Ewrapper class class TestApp (EClient, EWrapper):
class TestApp(EWrapper, EClient):
    def __init__(self):
        EClient.__init__(self, self)


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
