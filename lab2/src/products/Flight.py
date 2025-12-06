from uuid import uuid4
from src.techs.Validator import Validator
from src.techs.Date import Date
from typing import Optional
from src.products.Transport import Transport

class Flight:
    def __init__(self, code: str, departure: Date):
        Validator.validate_nonempty_str(code, "code")
        self.__id = str(uuid4())
        self.__code = code
        self.__departure = departure
        self.__transport: Optional[Transport] = None

    @property
    def id(self) -> str:
        return self.__id

    def assign_transport(self, transport: Transport) -> None:
        self.__transport = transport

    def reschedule(self, new_departure: Date) -> None:
        if new_departure <= self.__departure:
            raise ValueError("Новое время должно быть позже текущего")
        self.__departure = new_departure
