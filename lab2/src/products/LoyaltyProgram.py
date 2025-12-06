from uuid import uuid4
from src.techs.Validator import Validator
from src.finance.ClientWallet import ClientWallet

class LoyaltyProgram:
    def __init__(self, name: str):
        Validator.validate_nonempty_str(name, "name")
        self.__id = str(uuid4())
        self.__name = name
        self.__members: dict[str, ClientWallet] = {}

    def enroll(self, client_id: str) -> None:
        if client_id in self.__members:
            return
        self.__members[client_id] = ClientWallet(client_id)

    def add_points(self, client_id: str, points: float) -> None:
        if points <= 0:
            raise ValueError("points должен быть положительным")
        if client_id not in self.__members:
            self.enroll(client_id)
        self.__members[client_id].add_bonus(points)

    def get_balance(self, client_id: str) -> float:
        if client_id not in self.__members:
            return 0.0
        return float(self.__members[client_id].balance())

