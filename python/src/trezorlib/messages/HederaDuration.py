# Automatically generated by pb2py
# fmt: off
from .. import protobuf as p

if __debug__:
    try:
        from typing import Dict, List  # noqa: F401
        from typing_extensions import Literal  # noqa: F401
    except ImportError:
        pass


class HederaDuration(p.MessageType):

    def __init__(
        self,
        *,
        seconds: int = None,
    ) -> None:
        self.seconds = seconds

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('seconds', p.UVarintType, None),
        }
