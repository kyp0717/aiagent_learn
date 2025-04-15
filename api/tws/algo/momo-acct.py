import sys
from threading import Timer

from ibapi.client import Contract, EClient, OrderId
from ibapi.wrapper import EWrapper
from loguru import logger

logger.add(sys.stderr, level="TRACE")

port = 7500
bank = {}
position_ref = {}


class TestApp(EClient, EWrapper):
    def __init__(self):
        EClient.__init__(self, self)

    def nextValidId(self, orderId: OrderId):
        logger.info(f"Initial OrderId Created: {orderId}")
        self.orderId = orderId
        self.start()

    def nextId(self):
        self.orderId += 1
        return self.orderId

    def error(self, reqId, errorCode, errorString, advanceOrderReject):
        logger.error(
            f"ReqId: {reqId} --- ErrorCode: {errorCode}, ErrorString: {errorString}"
        )
        logger.error(f"ReqId: {reqId} --- Order Reject: {advanceOrderReject} ")

    def position(self, account, contract, position, avgCost):
        logger.info(account)
        logger.info(contract)
        logger.info(position)
        logger.info(avgCost)

    def updatePortfolio(
        self,
        contract: Contract,
        position: float,
        marketPrice: float,
        marketValue: float,
        averageCost: float,
        unrealizedPNL: float,
        realizedPNL: float,
        accountName: str,
    ):
        print(
            "UpdatePortfolio.",
            "Symbol:",
            contract.symbol,
            "SecType:",
            contract.secType,
            "Exchange:",
            contract.exchange,
            "Position:",
            position,
            "MarketPrice:",
            marketPrice,
            "MarketValue:",
            marketValue,
            "AverageCost:",
            averageCost,
            "UnrealizedPNL:",
            unrealizedPNL,
            "RealizedPNL:",
            realizedPNL,
            "AccountName:",
            accountName,
        )

    def updateAccountValue(self, key: str, val: str, currency: str, accountName: str):
        print(
            "UpdateAccountValue. Key:",
            key,
            "Value:",
            val,
            "Currency:",
            currency,
            "AccountName:",
            accountName,
        )

    def updateAccountTime(self, timeStamp: str):
        print("UpdateAccountTime. Time:", timeStamp)

    def accountDownloadEnd(self, accountName: str):
        print("AccountDownloadEnd. Account:", accountName)

    def start(self):
        # Account number can be omitted when using reqAccountUpdates with single account structure
        self.reqAccountUpdates(True, "")

    def stop(self):
        self.reqAccountUpdates(False, "")
        self.done = True
        self.disconnect()


def main():
    logger.info("Instantiate the app ...")
    app = TestApp()
    app.connect("127.0.0.1", 7497, 0)

    Timer(5, app.stop).start()
    app.run()


if __name__ == "__main__":
    main()
