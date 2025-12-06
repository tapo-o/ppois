from uuid import uuid4
from typing import Optional
from src.techs.Validator import Validator
from src.exceptions.exceptions import PaymentFailedException

class Payment:
    def __init__(self, amount: float):
        Validator.validate_positive_number(amount, "amount")
        self.__id: str = str(uuid4())
        self.__amount: float = float(amount)
        self.__status: str = "NEW"  # NEW, PROCESSING, PAID, FAILED, CANCELED
        self.__note: Optional[str] = None

    def id(self) -> str:
        return self.__id

    def amount(self) -> float:
        return self.__amount

    def status(self) -> str:
        return self.__status

    def note(self) -> Optional[str]:
        return self.__note

    def _set_status(self, new_status: str) -> None:
        if not isinstance(new_status, str) or not new_status:
            raise ValueError("new_status должен быть непустой строкой")
        self.__status = new_status

    def execute(self, system, card, pin: str) -> None:
        if self.__status not in ("NEW", "FAILED"):
            raise PaymentFailedException("Платёж нельзя выполнить в текущем статусе")
        try:
            system.process_payment(self, card, pin)
        except Exception as e:
            try:
                self._set_status("FAILED")
            except Exception:
                pass
            raise

    def cancel(self, reason: str) -> None:
        if self.__status == "PAID":
            raise PaymentFailedException("Нельзя отменить уже оплаченный платёж")
        self.__note = reason
        self.__status = "CANCELED"
