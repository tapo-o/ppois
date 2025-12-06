from uuid import uuid4
from typing import Optional
from src.techs.Validator import Validator
from src.exceptions.exceptions import BookingAlreadyExistsException

class Invoice:
    def __init__(self, number: Optional[str] = None):
        self.__id = str(uuid4())
        self.__number = number or str(uuid4())
        self.__amount = 0.0
        self.__client_email = ""
        self.__tour_id = ""
        self.__sent = False

    def id(self) -> str:
        return self.__id

    def number(self) -> str:
        return self.__number

    def amount(self) -> float:
        return self.__amount

    def generate(self, client: object, tour: object) -> None:
        Validator.validate_email(getattr(client, "email", ""))
        self.__client_email = client.email
        self.__tour_id = getattr(tour, "id", "")

        price_attr = getattr(tour, "price", None)

        if callable(price_attr):
            try:
                val = price_attr()
            except TypeError:
                try:
                    val = price_attr(tour)
                except TypeError:
                    try:
                        val = price_attr(getattr(tour, "id", None))
                    except Exception as e:
                        raise TypeError("Не удалось получить цену тура через price callable") from e
            except Exception as e:
                raise
            self.__amount = float(val)
        else:
            if hasattr(tour, "_Tour__price"):
                self.__amount = float(getattr(tour, "_Tour__price"))
            else:
                try:
                    self.__amount = float(getattr(tour, "price", 0.0))
                except Exception as e:
                    raise TypeError("Не удалось определить цену тура") from e

    def send(self) -> None:
        if self.__sent:
            raise BookingAlreadyExistsException("Инвойс уже отправлен")
        self.__sent = True

    def is_sent(self) -> bool:
        return self.__sent

    def client_email(self) -> str:
        return self.__client_email

    def tour_id(self) -> str:
        return self.__tour_id
