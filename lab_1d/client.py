from playground.network.packet import PacketType
import asyncio
import playground
from playground.asyncio_lib.testing import TestLoopEx
from playground.network.testing import MockTransportToProtocol
from playground.network.packet.fieldtypes import UINT32, STRING
import packetClass

class EchoClientProtocol(asyncio.Protocol):
    def __init__(self):
        #self.clientstatus = 0
        self.transport = None
        #self.deserializer = PacketType.Deserializer()

    def connection_made(self, transport):
        self.transport = transport
        self.deserializer = PacketType.Deserializer()
        # self.packet = RequestRecommandation()
        # RequestRecommandation().request = "request recommandation"
        # packetBytes = self.packet.__serialize__()
        # self.transport.write(packetBytes)
        print("Client is connected to server")
        firstRequest = packetClass.RequestRecommandation()
        self.Request(firstRequest)

    def Request(self,packet):
        if isinstance(packet,packetClass.RequestRecommandation):
            self.transport.write(packet.__serialize__())
        else:
            raise TypeError("wrong request")

    def data_received(self, data):
        self.deserializer.update(data)
        for pkt in self.deserializer.nextPackets():
            if isinstance(pkt, packetClass.Question):
                #self.clientstatus +=1
                print("Question packet received")
                OneAnswer = packetClass.Answer()
                OneAnswer.answer = "oliy"
                OneAnswer.ID = 1
                self.method(OneAnswer)
            elif isinstance(pkt, packetClass.Result):
                #self.clientstatus = 2
                print("Result packet received")
            else:
                print("finish")

    #method to get skintype
    def method(self,packet):
        self.transport.write(packet.__serialize__())

    def connection_lost(self, exc):
        print("connection lost")

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    coro = playground.getConnector().create_playground_connection (lambda:EchoClientProtocol(), '20174.1.1.1', 8888)
    loop.run_until_complete(coro)
    print (coro)
    print("Client Connected. Starting UI t:{}. p:{}")
    # request = packetClass.RequestRecommandation()
    # client = EchoClientProtocol()
    # client.Request(request)
    loop.run_forever()
    loop.close()

