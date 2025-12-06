from src.techs.Validator import Validator
from src.techs.Date import Date

class BookingCalendar:
    def __init__(self, title: str, timezone: str):
        Validator.validate_nonempty_str(title, "title")
        Validator.validate_nonempty_str(timezone, "timezone")
        self.__id = title
        self.__title = title
        self.__timezone = timezone
        self.__events: dict[str, str] = {}  # tour_id -> date_iso

    def add_event(self, tour: object, date: Date) -> None:
        self.__events[tour.id] = date.to_iso()

    def remove_event(self, tour: object) -> None:
        self.__events.pop(tour.id, None)

    def has_event(self, tour_id: str) -> bool:
        return tour_id in self.__events
