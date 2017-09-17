import playground
from playground.network.common import StackingProtocol,StackingTransport




class PassThrough1(StackingProtocol):
    def __init__(self):
        self.transport = None

    def connection_made(self, transport):
        print("1 connection made")
        trans = StackingTransport(transport)
        self.higherProtocol().connection_made(trans)


    def connection_lost(self,exc):
        self.higherProtocol().connection_lost(exc)
        print("1 connection lost")


    def data_received(self,data):
        self.higherProtocol().data_received(data)
        print("1 data received")

class PassThrough2(StackingProtocol):
    def __init__(self):
        self.transport = None

    def connection_made(self, transport):
        print("2 connection made")
        trans = StackingTransport(transport)
        self.higherProtocol().connection_made(trans)


    def connection_lost(self,exc):
        self.higherProtocol().connection_made(exc)
        print("2 connection lost")


    def data_received(self,data):
        self.higherProtocol().data_received(data)
        print("2 data received")






