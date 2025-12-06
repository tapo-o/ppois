from uuid import uuid4
from src.techs.Validator import Validator
from typing import List
from src.exceptions.exceptions import BookingAlreadyExistsException

class Supplier:
    def __init__(self, name: str, service_type: str):
        Validator.validate_nonempty_str(name, "name")
        Validator.validate_nonempty_str(service_type, "service_type")
        self.__id = str(uuid4())
        self.__name = name
        self.__service_type = service_type
        self.__contracts: List[str] = []

    def add_contract(self, contract_id: str) -> None:
        if contract_id in self.__contracts:
            raise BookingAlreadyExistsException("Контракт уже привязан")
        self.__contracts.append(contract_id)

    def rate(self, score: int) -> str:
        if not (1 <= score <= 5):
            raise ValueError("Оценка должна быть 1..5")
        return "high" if score >= 4 else "low"
