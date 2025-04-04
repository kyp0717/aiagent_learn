from ibapi.client import EClient
from ibapi.wrapper import EWrapper


class ScanApp(EClient, EWrapper):
    def __init__(self):
        EClient.__init__(self, self)

    def nextValidId(self, orderId):
        self.reqScannerParameters()

    def scannerParameters(self, xml):
        dir = "./scanner_parameters.xml"
        open(dir, "w").write(xml)


print("Writing parameters to xml file ...")
app = ScanApp()
app.connect("127.0.0.1", 7000, 1001)
app.run()
