from uuid import uuid4
from src.techs.Validator import Validator
from typing import Dict
from src.products.Room import Room
from src.techs.Date import Date

class Hotel:
    def __init__(self, name: str, address: str):
        Validator.validate_nonempty_str(name, "name")
        Validator.validate_nonempty_str(address, "address")
        self.__id = str(uuid4())
        self.__name = name
        self.__address = address
        self.__rooms: Dict[str, Room] = {}

    @property
    def id(self) -> str:
        return self.__id

    def add_room(self, room: Room) -> None:
        self.__rooms[room.id] = room

    def calculate_cost(self, nights: int, room: Room) -> float:
        if nights <= 0:
            raise ValueError("nights должно быть положительным")
        return nights * room._Room__price_per_night

    def check_availability(self, date_from: Date, date_to: Date) -> bool:
        for r in self.__rooms.values():
            for (f, t) in r._Room__booked_ranges:
                if not (date_to <= f or date_from >= t):
                    return False
        return True
