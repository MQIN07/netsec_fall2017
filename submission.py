from playground.network.packet import PacketType
from playground.network.packet.fieldtypes import UINT32, STRING


#class MyPacket(PacketType):
    #DEFINITION_IDENTIFIER = "lab2b.student_m.MyPacket"
    #DEFINITION_VERSION = "1.0"

    #FIELDS = [
     #           ("counter1", UINT32),
     #           ("counter2", UINT32),
      #          ("name", STRING),
                #("data", BUFFER)
   # ]

#packet1 = MyPacket()
#packet1.counter1 = 100
#packet1.counter2 = 200
#packet1.name = "Dr. Nielson"
#packet1.data = b'This may look like a string but it’s actually a sequence of bytes.'

#packetBytes = MyPacket.__serialize__(packet1)
#packetBytes = packet1.deserialize()
#print (packetBytes)


class RequestRecommandation(PacketType):
    DEFINITION_IDENTIFIER = "lab2b.student_m.RequuestRecommandation"
    DEFINITION_VERSION = "1.0"


class Question(PacketType):
    DEFINITION_IDENTIFIER = "lab2b.student_m.Question"
    DEFINITION_VERSION = "1.0"

    FIELDS = [
                ("ID", UINT32),
                ("ask", STRING),
    ]

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


def basicUnitTest():
    packet1 = RequestRecommandation()
    packet1Bytes = packet1.__serialize__()
    packet1a = RequestRecommandation.Deserialize(packet1Bytes)
    assert packet1 == packet1a

    packet2 = Question()
    packet2.ID = 1
    packet2.ask = "what is your skin type"
    packet2Bytes = packet2.__serialize__()
    packet2a = Question.Deserialize(packet2Bytes)
    assert packet2 == packet2a

    packet3 = Answer()
    #packet3.ID = -1   system error
    packet3.ID = 1
    packet3.answer = "oiliness"
    packet3Bytes = packet3.__serialize__()
    packet3a = Answer.Deserialize(packet3Bytes)
    assert packet3 == packet3a

    packet4 = Result()
    packet4.ID = 1
    packet4.product = "Clinique Liquid Facial Soup"
    packet4Bytes = packet4.__serialize__()
    packet4a = Answer.Deserializer()
    assert packet4 == packet4a

    if __name__=="__main__":
        basicUnitTest()
print("These two packets are the same!")

#pktBytes = packet1.__serialize__()+ packet2.__serialize__() + packet3.__serialize__() + packet4.__serialize__()
#packetTest = PacketType.Deserialize(pktBytes)
#if packet1 == packetTest:
