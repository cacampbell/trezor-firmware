# Automatically generated by pb2py
# fmt: off
import protobuf as p

from .OntologyTransaction import OntologyTransaction
from .OntologyTransfer import OntologyTransfer

if __debug__:
    try:
        from typing import List
    except ImportError:
        List = None  # type: ignore


class OntologySignTransfer(p.MessageType):
    MESSAGE_WIRE_TYPE = 354
    FIELDS = {
        1: ('address_n', p.UVarintType, p.FLAG_REPEATED),
        2: ('transaction', OntologyTransaction, 0),
        3: ('transfer', OntologyTransfer, 0),
    }

    def __init__(
        self,
        address_n: List[int] = None,
        transaction: OntologyTransaction = None,
        transfer: OntologyTransfer = None,
    ) -> None:
        self.address_n = address_n if address_n is not None else []
        self.transaction = transaction
        self.transfer = transfer