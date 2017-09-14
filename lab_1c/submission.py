from playground.network.packet import PacketType
import asyncio
# from playground.asyncio_lib.testing import TestLoopEx
from playground.network.testing import MockTransportToProtocol
from playground.network.packet.fieldtypes import UINT32, STRING
#from playground.common import logging as p_logging
import packetClass

class EchoServerProtocol(asyncio.Protocol):
    def __init__(self):
        self.serverstatus = 0
        self.transport = None

    def connection_made(self, transport):
        print ("Server is connected to client")
        self.transport = transport
        self.deserializer = PacketType.Deserializer()
        # self._deserializer = PacketType.Deserializer()

    def facetype(self,type):
        if type == "oily":
            return "Clinique Liquid Facial Soup"

    def data_received(self, data):
        #def RequestRecommandation()
        self.deserializer.update(data)
        for pkt in self.deserializer.nextPackets():
            if isinstance(pkt, packetClass.RequestRecommandation) and self.serverstatus == 0:
                print("recommandation request received")
                message = packetClass.Question()
                message.ID = 1
                message.ask = "what is your skin type"
                packet1Bytes = message.__serialize__()
                self.transport.write(packet1Bytes)
                self.serverstatus +=1
                break
            elif isinstance(pkt, packetClass.Answer) and self.serverstatus ==1:
                print("Answer packet received")
                mes = self.facetype(pkt.answer)
                rs = packetClass.Result()
                rs.ID = 1
                rs.product = mes
                self.transport.write(rs.__serialize__())
                self.serverstatus =2
                break
            else:
                print("No data received from client")
                self.transport.close()

    def connection_lost(self, exc):
        print("connection lost")

class EchoClientProtocol(asyncio.Protocol):
    def __init__(self):
        self.clientstatus = 0
        self.transport = None

    def connection_made(self, transport):
        self.transport = transport
        #self._deserializer = PacketType.Deserializer()
        # self.packet = RequestRecommandation()
        # RequestRecommandation().request = "request recommandation"
        # packetBytes = self.packet.__serialize__()
        # self.transport.write(packetBytes)
        print("Client is connected to server")
        self.deserializer = PacketType.Deserializer()

    # def test(self,packet):
    #     if isinstance(RequestRecommandation,packet):
    #

    def Request(self,packet):
        if isinstance(packet,packetClass.RequestRecommandation):
            # print(packet.__serialize__())
            self.transport.write(packet.__serialize__())

        else:
            #print("error")
            raise TypeError("wrong request")

    def data_received(self, data):

        self.deserializer.update(data)
        #clientstatus = 0
        #print(data)
        for pkt in self.deserializer.nextPackets():
            #print (pkt)
            if isinstance(pkt, packetClass.Question) and self.clientstatus == 0:
                self.clientstatus +=1
                print("Question packet received")
                break
            elif isinstance(pkt, packetClass.Result) and self.clientstatus == 1:
                self.clientstatus = 2
                print("Result packet received")
                break
            #     print(pkt.ask)
            #     self.transport.write(self.packet1Bytes)
            # elif isinstance(pkt, Result):
            #     print(pkt.product)
            #     self.transport.write(self.packet3Bytes)
            else:
                print("finish")
                self.transport.close()


    #method to get skintype
    def method(self,packet):
        self.transport.write(packet.__serialize__())

    def connection_lost(self, exc):
        print("connection lost")

def basicUnitTest():
    #asyncio.set_event_loop(TestLoopEx())
    # server = EchoServerProtocol()
    # client = EchoClientProtocol()
    # transportToServer = MockTransportToProtocol(server)
    # transportToClient = MockTransportToProtocol(client)
    # server.connection_made(transportToClient)
    # client.connection_made(transportToServer)
    client = EchoClientProtocol()
    server = EchoServerProtocol()
    cTransport, sTransport = MockTransportToProtocol.CreateTransportPair(client, server)
    client.connection_made(cTransport)
    server.connection_made(sTransport)
    firstRequest =  packetClass.RequestRecommandation()
    #firstRequest.request ="request connection"
    # firstRequest.request = None
    client.Request(firstRequest)
    assert server.serverstatus == 1
    assert client.clientstatus == 1
    #client.method(firstRequest)
    OneAnswer = packetClass.Answer()
    OneAnswer.answer = "oliy"
    OneAnswer.ID = 1
    client.method(OneAnswer)
    assert server.serverstatus == 2
    assert client.clientstatus == 2



if __name__=="__main__":
    #p_logging.EnablePresetLogging(p_logging.PRESET_TEST)
    basicUnitTest()





