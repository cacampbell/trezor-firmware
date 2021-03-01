# Automatically generated by pb2py
# fmt: off
import protobuf as p

if __debug__:
    try:
        from typing import Dict, List  # noqa: F401
        from typing_extensions import Literal  # noqa: F401
    except ImportError:
        pass


class HederaKey(p.MessageType):

    def __init__(
        self,
        *,
        ed25519: bytes = None,
    ) -> None:
        self.ed25519 = ed25519

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            2: ('ed25519', p.BytesType, None),
        }