from uuid import uuid4
from src.techs.Validator import Validator
from src.techs.Date import Date
from typing import Optional
from src.products.Flight import Flight

class Ticket:
    def __init__(self, number: str, departure: Date):
        Validator.validate_nonempty_str(number, "number")
        self.__id = str(uuid4())
        self.__number = number
        self.__departure = departure
        self.__flight: Optional[Flight] = None

    @property
    def id(self) -> str:
        return self.__id

    def assign_flight(self, flight: Flight) -> None:
        self.__flight = flight

    def change_date(self, new_date: Date) -> None:
        if new_date <= self.__departure:
            raise ValueError("Новая дата должна быть позже текущей")
        self.__departure = new_date
