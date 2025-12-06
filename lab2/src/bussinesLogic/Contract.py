from uuid import uuid4
from typing import Optional
from src.techs.Validator import Validator
from src.techs.Date import Date
from src.exceptions.exceptions import ContractViolationException

class Contract:
    def __init__(self, number: str):
        Validator.validate_nonempty_str(number, "number")
        self.__id = str(uuid4())
        self.__number = number
        self.__signed_at: Optional[Date] = None
        self.__client_id: Optional[str] = None
        self.__manager_id: Optional[str] = None
        self.__active: bool = False

    def id(self) -> str:
        return self.__id

    def number(self) -> str:
        return self.__number

    def is_active(self) -> bool:
        return self.__active

    def sign(self, client: object, manager: object, signed_at: Optional[Date] = None) -> None:
        if self.__active:
            raise ContractViolationException("Договор уже активен")
        self.__client_id = getattr(client, "id", None)
        self.__manager_id = getattr(manager, "id", None)
        self.__signed_at = signed_at or Date(1, 1, 2025)
        self.__active = True

    def terminate(self, reason: str) -> None:
        self.__active = False
