from typing import List, Tuple
from src.techs.Validator import Validator
from src.exceptions.exceptions import BookingAlreadyExistsException, TourNotFoundException

class BookingSystem:
    def __init__(self, version: str):
        Validator.validate_nonempty_str(version, "version")
        self.__version = version
        self.__bookings: List[Tuple[str, str]] = []  # (client_id, tour_id)

    def create_booking(self, client: object, tour: object) -> None:
        key = (client.id, tour.id)
        if key in self.__bookings:
            raise BookingAlreadyExistsException("Бронь уже существует")
        client.book_tour(tour)
        self.__bookings.append(key)

    def cancel_booking(self, client: object, tour: object) -> None:
        key = (client.id, tour.id)
        if key not in self.__bookings:
            raise TourNotFoundException("Бронь не найдена")
        self.__bookings.remove(key)

    def is_booked(self, client_id: str, tour_id: str) -> bool:
        return (client_id, tour_id) in self.__bookings

    def list_bookings(self) -> List[Tuple[str, str]]:
        return list(self.__bookings)
