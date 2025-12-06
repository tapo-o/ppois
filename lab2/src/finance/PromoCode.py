from src.techs.Validator import Validator
from src.techs.Date import Date
from src.exceptions.exceptions import ContractViolationException, BookingAlreadyExistsException

class PromoCode:
    def __init__(self, code: str, percent: float, expires: Date):
        Validator.validate_nonempty_str(code, "code")
        if not (0 <= percent <= 100):
            raise ValueError("percent должен быть в диапазоне 0..100")
        self.__code = code
        self.__percent = float(percent)
        self.__expires = expires
        self.__active = True
        self.__used_by: list[str] = []

    def code(self) -> str:
        return self.__code

    def activate_for(self, client: object) -> None:
        if not self.__active:
            raise ContractViolationException("Промокод не активен")
        if self.__expires < Date(1,1,1970): 
            raise ContractViolationException("Промокод истёк")
        if client.id in self.__used_by:
            raise BookingAlreadyExistsException("Промокод уже использован этим клиентом")
        self.__used_by.append(client.id)

    def apply(self, amount: float) -> float:
        if not self.__active:
            raise ContractViolationException("Промокод не активен")
        discount = amount * (self.__percent / 100.0)
        return max(0.0, amount - discount)

    def deactivate(self) -> None:
        self.__active = False
