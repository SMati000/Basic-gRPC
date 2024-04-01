from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Mensaje(_message.Message):
    __slots__ = ("printThis",)
    PRINTTHIS_FIELD_NUMBER: _ClassVar[int]
    printThis: str
    def __init__(self, printThis: _Optional[str] = ...) -> None: ...
