from playground.network.packet import PacketType
import asyncio
import playground
from playground.asyncio_lib.testing import TestLoopEx
from playground.network.testing import MockTransportToProtocol
from playground.network.packet.fieldtypes import UINT32, STRING
import packetClass
import playground
from playground.network.common import StackingProtocolFactory
from submission import PassThrough1, PassThrough2
import logging

class EchoServerProtocol(asyncio.Protocol):
    def __init__(self):
        #self.serverstatus = 0
        self.transport = None

    def connection_made(self, transport):
        print ("Server is connected to client")
        self.transport = transport
        peername = transport.get_extra_info('peername')
        print('Build Connection from {}'.format(peername))
        self.deserializer = PacketType.Deserializer()

    def facetype(self,type):
        if type == "oily":
            return "Clinique Liquid Facial Soup"

    def data_received(self, data):
        #def RequestRecommandation()
        self.deserializer.update(data)
        for pkt in self.deserializer.nextPackets():
            if isinstance(pkt, packetClass.RequestRecommandation):
                print("recommandation request received")
                message = packetClass.Question()
                message.ID = 1
                message.ask = "what is your skin type"
                packet1Bytes = message.__serialize__()
                self.transport.write(packet1Bytes)
                #self.serverstatus +=1
            elif isinstance(pkt, packetClass.Answer):
                print("Answer packet received")
                mes = self.facetype(pkt.answer)
                rs = packetClass.Result()
                rs.ID = 1
                rs.product = mes
                self.transport.write(rs.__serialize__())
            else:
                print("No data received from client")
                self.transport.close()

    # def sendRequest(self,request):
    #     self.transport.write(request.__serialize__())

if __name__ == "__main__":
    f = StackingProtocolFactory(lambda: PassThrough1(), lambda: PassThrough2())
    ptConnector = playground.Connector(protocolStack=f)
    playground.setConnector("passthrough", ptConnector)
    loop = asyncio.get_event_loop()
    coro = playground.getConnector('passthrough').create_playground_server(EchoServerProtocol, 8888)
    server = loop.run_until_complete(coro)
    print("Echo Server Started at {}".format(server.sockets[0].gethostname()))
    loop.run_forever()
    loop.close()
