from uuid import uuid4
from src.techs.Validator import Validator
from src.exceptions.exceptions import PaymentFailedException

class RefundProcessor:
    def __init__(self):
        self.__id = str(uuid4())
        self.__processed: list[str] = []

    def process_refund(self, payment, amount: float) -> None:
        if getattr(payment, "status", lambda: None)() != "PAID":
            raise PaymentFailedException("Платёж не оплачен")
        if amount <= 0:
            raise ValueError("amount должен быть положительным")
        self.__processed.append(getattr(payment, "id", "unknown"))
