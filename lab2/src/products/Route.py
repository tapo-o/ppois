from uuid import uuid4
from src.techs.Validator import Validator

class Route:
    def __init__(self, description: str, length_km: float):
        Validator.validate_nonempty_str(description, "description")
        self.__id = str(uuid4())
        self.__description = description
        self.__length_km = float(length_km)
        self.__points = []

    @property
    def id(self) -> str:
        return self.__id

    def add_point(self, point: str) -> None:
        Validator.validate_nonempty_str(point, "point")
        self.__points.append(point)

    def optimize(self, transport) -> None:
        if transport.capacity() < 10:
            self.__length_km *= 0.95

