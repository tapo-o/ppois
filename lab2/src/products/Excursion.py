from uuid import uuid4
from src.techs.Validator import Validator
from typing import Optional

class Excursion:
    def __init__(self, title: str, duration_hours: int):
        Validator.validate_nonempty_str(title, "title")
        self.__id = str(uuid4())
        self.__title = title
        self.__duration_hours = int(duration_hours)
        self.__route: Optional[object] = None
        self.__guide_id: Optional[str] = None

    @property
    def id(self) -> str:
        return self.__id

    def set_guide_id(self, gid: str) -> None:
        self.__guide_id = gid

    def assign_guide(self, guide) -> None:
        self.__guide_id = guide.id

    def add_route(self, route) -> None:
        self.__route = route
