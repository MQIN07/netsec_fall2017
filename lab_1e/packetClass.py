from playground.network.packet import PacketType
from playground.network.packet.fieldtypes import UINT32, STRING

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
