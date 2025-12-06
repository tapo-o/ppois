from typing import Dict, List
from uuid import uuid4
from src.techs.Validator import Validator
from src.exceptions.exceptions import TourNotFoundException

class TourCatalog:
    def __init__(self, title: str):
        Validator.validate_nonempty_str(title, "title")
        self.__id = str(uuid4())
        self.__title = title
        self.__tours: Dict[str, object] = {}  # Tour instances

    @property
    def id(self) -> str:
        return self.__id

    def title(self) -> str:
        return self.__title

    def add_tour(self, tour: object) -> None:
        self.__tours[tour.id] = tour

    def remove_tour(self, tour_id: str) -> None:
        if tour_id not in self.__tours:
            raise TourNotFoundException("Тур отсутствует в каталоге")
        del self.__tours[tour_id]

    def list_tours(self) -> List[object]:
        return list(self.__tours.values())

    def find_by_id(self, tour_id: str) -> object:
        return self.__tours.get(tour_id)
