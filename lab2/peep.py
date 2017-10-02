from playground.network.common import StackingProtocol
from peeptransport import PEEPTransport

from playground.network.packet import PacketType
import asyncio
from playground.network.testing import MockTransportToProtocol
from playground.network.common import StackingProtocol,StackingTransport
from packetClass import *

import playground

class PEEPClient(asyncio.Protocol):

    def __init__(self):
        super().__init__()
        self.data = None

        # The state is to identify whether the packet type.
        #self.state = -1

    def connection_made(self, transport):
        print('--- peep connect to server ---')
        self.transport = transport
        self.deserializer = PacketType.Deserializer()
        peepInfoC = PEEPPacket()
        peepInfoC.sequenceNumber = 1
        #peepInfo.Acknowledgement =
        self.transport.write(peepInfoC.__serialize__())


    # def data_received(self, data):

    # def connection_lost(self, exc):
    #     self.connection_lost(exc)
class PEEPServer(StackingProtocol):

    def __init__(self):
        super().__init__()
        self.data = None

        # The state is to identify whether the packet type.
        self.state = -1

    def connection_made(self, transport):
        print('--- peep connect to client---')
        self.transport = transport
        self.deserializer = PacketType.Deserializer()

    def data_received(self, data):
        self.deserializer.update(data)
        print (data)
        # peepInfoS = PEEPPacket()
        # peepInfoS.sequenceNumber = 5
        # for pkt in self.deserializer.nextPackets():
        #     if isinstance(pkt,PEEPClient.connection_made().peepInfoC.sequenceNumber()):
        #         peepInfoS.Acknowledgement = PEEPClient.connection_made().peepInfoC.sequenceNumber()+1
        #         self.transport.write(peepInfoS.__serialize__())

    def connection_lost(self, exc):
        self.connection_lost(exc)


if __name__ == '__main__':
    client = PEEPClient()
    server = PEEPServer()
    cTransport, sTransport = MockTransportToProtocol.CreateTransportPair(client, server)
    client.connection_made(cTransport)
    server.connection_made(sTransport)




