from uuid import uuid4
from src.techs.Validator import Validator
from typing import List, Optional
from src.products.Hotel import Hotel
from src.products.Route import Route

class Tour:
    def __init__(self, title: str, price: float):
        Validator.validate_nonempty_str(title, "title")
        if price < 0:
            raise ValueError("price не может быть отрицательной")
        self.__id = str(uuid4())
        self.__title = title
        self.__price = float(price)
        self.__hotel: Optional[Hotel] = None
        self.__routes: List[Route] = []

    @property
    def id(self) -> str:
        return self.__id

    def price(self) -> float:
        return self.__price

    def assign_hotel(self, hotel: Hotel) -> None:
        self.__hotel = hotel

    def add_route(self, route: Route) -> None:
        self.__routes.append(route)
