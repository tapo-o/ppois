from src.techs.Validator import Validator
from src.exceptions.exceptions import InsufficientFundsException

class ClientWallet:
    def __init__(self, client_id: str):
        Validator.validate_nonempty_str(client_id, "client_id")
        self.__id = client_id
        self.__bonus_balance = 0.0

    def balance(self) -> float:
        return self.__bonus_balance

    def add_bonus(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("amount должен быть положительным")
        self.__bonus_balance += amount

    def spend_bonus(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("amount должен быть положительным")
        if self.__bonus_balance < amount:
            raise InsufficientFundsException("Недостаточно бонусов")
        self.__bonus_balance -= amount
