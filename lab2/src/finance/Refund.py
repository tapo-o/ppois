from uuid import uuid4
from src.techs.Validator import Validator
from src.exceptions.exceptions import PaymentFailedException

class Refund:
    def __init__(self, amount: float, reason: str):
        Validator.validate_nonempty_str(reason, "reason")
        if amount <= 0:
            raise ValueError("amount должен быть положительным")
        self.__id = str(uuid4())
        self.__amount = float(amount)
        self.__reason = reason
        self.__approved = False
        self.__processed_at = None

    def initiate(self, payment) -> None:
        if getattr(payment, "status", lambda: None)() != "PAID":
            raise PaymentFailedException("Возврат возможен только по оплаченным платежам")
        self.__approved = True

    def confirm(self) -> None:
        if not self.__approved:
            raise PaymentFailedException("Возврат не одобрен")
        self.__processed_at = "2025-01-01T00:00:00"
