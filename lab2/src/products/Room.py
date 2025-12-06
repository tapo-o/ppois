from uuid import uuid4
from src.techs.Validator import Validator
from typing import List, Tuple
from src.techs.Date import Date
from src.exceptions.exceptions import HotelNotAvailableException

class Room:
    def __init__(self, room_type: str, price_per_night: float):
        Validator.validate_nonempty_str(room_type, "room_type")
        self.__id = str(uuid4())
        self.__room_type = room_type
        self.__price_per_night = float(price_per_night)
        self.__booked_ranges: List[Tuple[Date, Date]] = []

    @property
    def id(self) -> str:
        return self.__id

    def book(self, client, date_from: Date, date_to: Date) -> None:
        if not isinstance(date_from, Date) or not isinstance(date_to, Date):
            raise ValueError("date_from и date_to должны быть Date")
        if date_to <= date_from:
            raise ValueError("date_to должен быть позже date_from")
        for (f, t) in self.__booked_ranges:
            if (date_from < t) and (f < date_to):
                raise HotelNotAvailableException("Номер недоступен на выбранные даты")
        self.__booked_ranges.append((date_from, date_to))

    def update_price(self, new_price: float) -> None:
        if new_price <= 0:
            raise ValueError("Цена должна быть положительной")
        self.__price_per_night = float(new_price)
