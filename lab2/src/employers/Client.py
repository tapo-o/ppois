from typing import List
from uuid import uuid4
from src.techs.Validator import Validator

class Client:
    def __init__(self, name: str, email: str):
        Validator.validate_nonempty_str(name, "name")
        Validator.validate_email(email)
        self.__id = str(uuid4())
        self.__name = name
        self.__email = email
        self.__cards: List[object] = []      # BankCard
        self.__booked_tours: List[str] = []  # тур ids

    @property
    def id(self) -> str:
        return self.__id

    @property
    def name(self) -> str:
        return self.__name

    @property
    def email(self) -> str:
        return self.__email

    def get_cards(self) -> List[object]:
        return list(self.__cards)

    def get_bookings(self) -> List[str]:
        return list(self.__booked_tours)

    # Добавляет тур в список бронирований или бросает исключение при дубликате  
    def book_tour(self, tour) -> None:
        if tour.id in self.__booked_tours:
            from src.exceptions.exceptions import BookingAlreadyExistsException
            raise BookingAlreadyExistsException("Клиент уже забронировал этот тур")
        self.__booked_tours.append(tour.id)

    # Привязывает карту к клиенту после проверки валидности email
    def attach_card(self, card) -> None:
        Validator.validate_email(self.__email)
        self.__cards.append(card)

    # Помечает клиента как заблокированного, модифицируя отображаемое имя
    def _mark_blocked(self) -> None:
        self.__name = "[BLOCKED] " + self.__name
