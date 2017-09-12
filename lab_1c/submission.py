from playground.network.packet import PacketType
import asyncio
from playground.asyncio_lib.testing import TestLoopEx
from playground.network.testing import MockTransportToProtocol
from playground.network.packet.fieldtypes import UINT32, STRING

class RequestRecommandation(PacketType):
    DEFINITION_IDENTIFIER = "lab2b.student_m.RequestRecommandation"
    DEFINITION_VERSION = "1.0"
    FIELDS = [
        ("request", STRING)
    ]

class Question(PacketType):
    DEFINITION_IDENTIFIER = "lab2b.student_m.Question"
    DEFINITION_VERSION = "1.0"

    FIELDS = [
                ("ID", UINT32),
                ("ask", STRING),
    ]
    #self._item = packType
    #self.transport.write()

class Answer(PacketType):
    DEFINITION_IDENTIFIER = "lab2b.student_m.Answer"
    DEFINITION_VERSION = "1.0"

    FIELDS = [
                ("ID", UINT32),
                ("answer", STRING),
    ]

class Result(PacketType):
    DEFINITION_IDENTIFIER = "lab2b.student_m.Result"
    DEFINITION_VERSION = "1.0"

    FIELDS = [
                ("ID", UINT32),
                ("product", STRING),
    ]


class EchoServerProtocol(asyncio.Protocol):
    def __init__(self):
        self.serverstatus = 0
        self.transport = None

    def connection_made(self, transport):
        print ("Server is connected to client")
        self.transport = transport
        self.deserializer = PacketType.Deserializer()

    def facetype(self,type):
        if type == "oily":
            return "Clinique Liquid Facial Soup"

    def data_received(self, data):
        #def RequestRecommandation()
        self.deserializer.update(data)
        for pkt in self.deserializer.nextPackets():
            if isinstance(pkt, RequestRecommandation) and self.serverstatus == 0:
                print("recommandation request received")
                message = Question()
                message.ID = 1
                message.ask = "what is your skin type"
                packet1Bytes = message.__serialize__()
                self.transport.write(packet1Bytes)
                self.serverstatus +=1
                break
            elif isinstance(pkt, Answer) and self.serverstatus ==1:
                print("Answer packer received")
                mes = self.facetype(pkt.answer)
                rs = Result()
                rs.ID = 1
                rs.product = mes
                self.transport.write(rs.__serialize__())
                self.serverstatus =2
                break
            else:
                print("No data received from client")

class EchoClientProtocol(asyncio.Protocol):
    def __init__(self):
        self.clientstatus = 0
        self.transport = None
        self.deserializer = PacketType.Deserializer()

    def connection_made(self, transport):
        self.transport = transport
        #self._deserializer = PacketType.Deserializer()
        # self.packet = RequestRecommandation()
        # RequestRecommandation().request = "request recommandation"
        # packetBytes = self.packet.__serialize__()
        # self.transport.write(packetBytes)
        print("Client is connected to server")

    # def test(self,packet):
    #     if isinstance(RequestRecommandation,packet):
    #

    def Request(self,packet):
        if isinstance(packet,RequestRecommandation):
            self.transport.write(packet.__serialize__())

        else:
            #print("error")
            raise TypeError("wrong request")

    #def input(self,skintype):
        #self.skintype = skintype

        #if isinstance(self.skintype, skintype):
         #   print("Clinique Liquid Facial Soup")

       # self.transport.write(self.skintype)



    def data_received(self, data):

        self.deserializer.update(data)
        #clientstatus = 0

        #print(data)
        for pkt in self.deserializer.nextPackets():
            if isinstance(pkt, Question) and self.clientstatus == 0:
                self.clientstatus +=1
                break

            elif isinstance(pkt, Result) and self.clientstatus == 1:
                self.clientstatus = 2
                break
            #     print(pkt.ask)
            #     self.transport.write(self.packet1Bytes)
            # elif isinstance(pkt, Result):
            #     print(pkt.product)
            #     self.transport.write(self.packet3Bytes)
            else:
                print("finish")


    #method to get skintype
    def method(self,packet):
        self.transport.write(packet.__serialize__())

    def connection_lost(self, exc):
        print("connection lost")

def basicUnitTest():
    asyncio.set_event_loop(TestLoopEx())
    server = EchoServerProtocol()
    client = EchoClientProtocol()
    transportToServer = MockTransportToProtocol(server)
    transportToClient = MockTransportToProtocol(client)
    server.connection_made(transportToClient)
    client.connection_made(transportToServer)
    firstRequest =  RequestRecommandation()
    firstRequest.request ="request connection"
    client.Request(firstRequest)
    assert server.serverstatus == 1
    assert client.clientstatus == 1
    #client.method(firstRequest)
    OneAnswer = Answer()
    OneAnswer.answer = "oliy"
    OneAnswer.ID = 1
    client.method(OneAnswer)
    assert server.serverstatus == 2
    assert client.clientstatus == 2



if __name__=="__main__":
    basicUnitTest()





