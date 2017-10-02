from playground.network.packet import PacketType
from playground.network.packet.fieldtypes import UINT32, STRING

from playground.network.packet import *
from playground.network.packet.fieldtypes import UINT32, UINT8, UINT16, BUFFER
from playground.network.packet.fieldtypes.attributes import *
from playground.network.packet import PacketType
import asyncio


class PEEPPacket(PacketType):
    DEFINITION_IDENTIFIER = "PEEP.Packet"
    DEFINITION_VERSION = "1.0"

    FIELDS = [

        # ("Type", UINT8),

        ("SequenceNumber", UINT32({Optional: True})),
        # ("Checksum", UINT16),

        ("Acknowledgement", UINT32({Optional: True})),

        ("Data", BUFFER({Optional: True}))
    ]
