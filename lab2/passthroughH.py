import playground
from playground.network.common import StackingProtocol, StackingTransport

class PassThroughHServer(StackingProtocol):
    def __init__(self):
        self.transport = None

    def connection_made(self, transport):
        print("2 connection made")
        trans = StackingTransport(transport)
        self.higherProtocol().connection_made(trans)

    def connection_lost(self, exc):
        self.higherProtocol().connection_lost(exc)

    def data_received(self, data):
        self.higherProtocol().data_received(data)
        print("2 data received")

class PassThroughHClient(StackingProtocol):
    def __init__(self):
        self.transport = None

    def connection_made(self, transport):
        print("2 connection made")
        trans = StackingTransport(transport)
        self.higherProtocol().connection_made(trans)

    def connection_lost(self, exc):
        self.higherProtocol().connection_lost(exc)

    def data_received(self, data):
        self.higherProtocol().data_received(data)
        print("2 data received")