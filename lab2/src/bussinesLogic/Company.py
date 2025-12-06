from uuid import uuid4
from typing import Dict, Optional
from src.techs.Validator import Validator
from src.employers.Client import Client
from src.bussinesLogic.Contract import Contract
from src.exceptions.exceptions import InvalidEmailException

class Company:
    def __init__(self, name: str, legal_address: str):
        Validator.validate_nonempty_str(name, "name")
        Validator.validate_nonempty_str(legal_address, "legal_address")
        self.__id = str(uuid4())
        self.__name = name
        self.__legal_address = legal_address
        self.__clients: Dict[str, Client] = {}
        self.__contracts: Dict[str, Contract] = {}
        self.__departments: Dict[str, object] = {}

    def id(self) -> str:
        return self.__id

    # Добавляет клиента после валидации email, иначе бросает InvalidEmailException
    def add_client(self, client: Client) -> None:
        try:
            Validator.validate_email(client.email)
        except Exception as e:
            raise InvalidEmailException(str(e))
        self.__clients[client.id] = client

    def get_client(self, client_id: str) -> Optional[Client]:
        return self.__clients.get(client_id)

    def clients(self) -> Dict[str, Client]:
        return dict(self.__clients)

    # Подписывает контракт и сохраняет его в реестре контрактов
    def sign_contract(self, contract: Contract, client: Client, manager: object) -> None:
        contract.sign(client, manager)
        self.__contracts[contract.id()] = contract

    def contracts(self) -> Dict[str, Contract]:
        return dict(self.__contracts)

    def add_department(self, dept: object) -> None:
        dept_id = getattr(dept, "id", None) or getattr(dept, "_Department__id", None)
        if dept_id is None:
            dept_id = str(uuid4())
        self.__departments[dept_id] = dept

    def departments(self) -> Dict[str, object]:
        return dict(self.__departments)
