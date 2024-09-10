from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class CalculoIMCRequest(_message.Message):
    __slots__ = ("nome", "peso", "altura")
    NOME_FIELD_NUMBER: _ClassVar[int]
    PESO_FIELD_NUMBER: _ClassVar[int]
    ALTURA_FIELD_NUMBER: _ClassVar[int]
    nome: str
    peso: float
    altura: float
    def __init__(self, nome: _Optional[str] = ..., peso: _Optional[float] = ..., altura: _Optional[float] = ...) -> None: ...

class CalculoIMCResponse(_message.Message):
    __slots__ = ("aviso", "imc")
    AVISO_FIELD_NUMBER: _ClassVar[int]
    IMC_FIELD_NUMBER: _ClassVar[int]
    aviso: str
    imc: float
    def __init__(self, aviso: _Optional[str] = ..., imc: _Optional[float] = ...) -> None: ...
