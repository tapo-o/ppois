from src.techs.Validator import Validator
from src.exceptions.exceptions import InsufficientFundsException

class Account:
    def __init__(self, owner_id: str, currency_code: str = "BYN"):
        Validator.validate_nonempty_str(owner_id, "owner_id")
        self.__id = owner_id
        self.__owner_id = owner_id
        self.__balance = 0.0
        self.__currency_code = currency_code

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("amount должен быть положительным")
        self.__balance += amount

    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("amount должен быть положительным")
        if self.__balance < amount:
            raise InsufficientFundsException("Недостаточно средств")
        self.__balance -= amount

    def balance(self) -> float:
        return self.__balance
