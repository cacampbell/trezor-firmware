# Automatically generated by pb2py
# fmt: off
import protobuf as p

from .HederaTokenTransferList import HederaTokenTransferList
from .HederaTransferList import HederaTransferList

if __debug__:
    try:
        from typing import Dict, List  # noqa: F401
        from typing_extensions import Literal  # noqa: F401
    except ImportError:
        pass


class HederaCryptoTransferTransactionBody(p.MessageType):

    def __init__(
        self,
        *,
        tokenTransfers: List[HederaTokenTransferList] = None,
        transfers: HederaTransferList = None,
    ) -> None:
        self.tokenTransfers = tokenTransfers if tokenTransfers is not None else []
        self.transfers = transfers

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('transfers', HederaTransferList, None),
            2: ('tokenTransfers', HederaTokenTransferList, p.FLAG_REPEATED),
        }
