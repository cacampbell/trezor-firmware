# Automatically generated by pb2py
# fmt: off
from .. import protobuf as p

from .HederaAccountAmount import HederaAccountAmount
from .HederaId import HederaId

if __debug__:
    try:
        from typing import Dict, List  # noqa: F401
        from typing_extensions import Literal  # noqa: F401
    except ImportError:
        pass


class HederaTokenTransferList(p.MessageType):

    def __init__(
        self,
        *,
        accountAmounts: List[HederaAccountAmount] = None,
        token: HederaId = None,
    ) -> None:
        self.accountAmounts = accountAmounts if accountAmounts is not None else []
        self.token = token

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('token', HederaId, None),
            2: ('accountAmounts', HederaAccountAmount, p.FLAG_REPEATED),
        }
