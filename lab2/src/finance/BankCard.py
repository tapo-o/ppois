from typing import Any
from src.techs.Validator import Validator
from src.techs.Date import Date
from src.exceptions.exceptions import InvalidPasswordException, InsufficientFundsException, CardExpiredException

class BankCard:
    def __init__(self, number: str, balance: float, expiry: Any, pin: str):
        Validator.validate_nonempty_str(number, "number")
        if isinstance(expiry, Date):
            self.__expiry = expiry
        elif isinstance(expiry, str):
            self.__expiry = Date.from_iso(expiry)
        else:
            raise ValueError("expiry должен быть объектом Date или ISO-строкой YYYY-MM-DD")
        if balance < 0:
            raise ValueError("balance не может быть отрицательным")
        Validator.validate_nonempty_str(pin, "pin")

        self.__number: str = number
        self.__balance: float = float(balance)
        self.__pin: str = pin

    @property
    def number(self) -> str:
        return self.__number

    def balance(self) -> float:
        return float(self.__balance)

    def check_pin(self, pin: str) -> bool:
        if self.__pin != pin:
            raise InvalidPasswordException("Неверный PIN")
        return True

    # Проверяет, что срок действия карты ещё не истёк
    def ensure_not_expired(self) -> None:
        if not isinstance(self.__expiry, Date):
            raise ValueError("expiry некорректен")
        if self.__expiry <= Date.today():
            raise CardExpiredException("Срок действия карты истёк")

    # Переводит сумму на другую карту после проверки PIN, баланса и валидности аргументов
    def transfer_to(self, other: "BankCard", amount: float, pin: str) -> None:
        if not isinstance(other, BankCard):
            raise ValueError("other должен быть BankCard")
        if amount <= 0:
            raise ValueError("amount должен быть положительным")
        self.check_pin(pin)
        if self.__balance < amount:
            raise InsufficientFundsException("Недостаточно средств")
        self.__balance -= float(amount)
        other._receive(float(amount))

    # Внутренний метод приёма средств на карту
    def _receive(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("amount должен быть положительным")
        self.__balance += float(amount)

    def set_pin(self, old_pin: str, new_pin: str) -> None:
        if self.__pin != old_pin:
            raise InvalidPasswordException("Старый PIN неверен")
        Validator.validate_nonempty_str(new_pin, "new_pin")
        self.__pin = new_pin

    def expiry(self) -> Date:
        return self.__expiry
