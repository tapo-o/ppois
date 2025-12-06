from uuid import uuid4
from src.techs.Validator import Validator
from typing import Optional
from src.products.Route import Route
from src.exceptions.exceptions import TransportDelayException

class Transport:
    def __init__(self, transport_type: str, capacity: int):
        Validator.validate_nonempty_str(transport_type, "transport_type")
        self.__id = str(uuid4())
        self.__transport_type = transport_type
        self.__capacity = int(capacity)
        self.__route: Optional[Route] = None
        self.__technical_ok = True

    @property
    def id(self) -> str:
        return self.__id

    def capacity(self) -> int:
        return self.__capacity

    def assign_route(self, route: Route) -> None:
        self.__route = route

    def check_technical_condition(self) -> None:
        if not self.__technical_ok:
            raise TransportDelayException("Транспорт неисправен")
