from uuid import uuid4
from src.techs.Validator import Validator
from src.products.Review import Review

class HotelRating:
    def __init__(self, stars: int):
        if not (1 <= stars <= 5):
            raise ValueError("stars должен быть 1..5")
        self.__id = str(uuid4())
        self.__stars = int(stars)
        self.__comments: list[str] = []

    def add_review(self, review: Review) -> None:
        self.__comments.append(getattr(review, "_Review__text", ""))

    def recalc_average(self) -> float:
        avg = max(1.0, self.__stars - 0.1 * len(self.__comments))
        return avg
