from typing import Optional
from uuid import uuid4
from src.techs.Validator import Validator
from src.finance.BankCard import BankCard
from src.finance.Payment import Payment
from src.techs.Date import Date
from src.exceptions.exceptions import PaymentFailedException, InsufficientFundsException, InvalidPasswordException

class PaymentSystem:
    def __init__(self, provider: str, commission_percent: float = 0.0):
        Validator.validate_nonempty_str(provider, "provider")
        if commission_percent < 0:
            raise ValueError("commission_percent не может быть отрицательным")
        self.__id = str(uuid4())
        self.__provider = provider
        self.__commission_percent = float(commission_percent)
        self.__processed_payments: dict[str, str] = {}  # payment_id -> status

    @property
    def id(self) -> str:
        return self.__id

    @property
    def provider(self) -> str:
        return self.__provider

    def commission_percent(self) -> float:
        return self.__commission_percent

    def _calculate_total(self, amount: float) -> float:
        return amount * (1.0 + self.__commission_percent / 100.0)

    def process_payment(self, payment: Payment, card: BankCard, pin: str, system_wallet: Optional[BankCard] = None) -> None:
        if not isinstance(payment, Payment):
            raise ValueError("payment должен быть Payment")
        if not isinstance(card, BankCard):
            raise ValueError("card должен быть BankCard")

        if payment.status() not in ("NEW", "FAILED"):
            raise PaymentFailedException("Платёж нельзя выполнить в текущем статусе")

        total = self._calculate_total(payment.amount())
        if system_wallet is None:
            system_wallet = BankCard("SYS-" + str(uuid4()), 0.0, Date(31, 12, 2099), "0000")

        try:
            card.transfer_to(system_wallet, total, pin)
            payment._set_status("PAID")
            self.__processed_payments[payment.id()] = "PAID"
        except InvalidPasswordException as e:
            payment._set_status("FAILED")
            self.__processed_payments[payment.id()] = "FAILED"
            raise
        except InsufficientFundsException as e:
            payment._set_status("FAILED")
            self.__processed_payments[payment.id()] = "FAILED"
            raise
        except Exception as e:
            payment._set_status("FAILED")
            self.__processed_payments[payment.id()] = "FAILED"
            raise PaymentFailedException(f"Ошибка при обработке платежа: {e}")

    def last_status(self, payment: Payment) -> Optional[str]:
        return self.__processed_payments.get(payment.id())
