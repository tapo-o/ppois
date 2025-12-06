from __future__ import annotations
from datetime import date as _date

class Date:
    __slots__ = ("__day", "__month", "__year")

    def __init__(self, day: int, month: int, year: int):
        if not (1 <= month <= 12):
            raise ValueError("Месяц должен быть в диапазоне 1..12")
        if not (1 <= day <= 31):
            raise ValueError("День должен быть в диапазоне 1..31")
        if year < 0:
            raise ValueError("Год должен быть неотрицательным")
        self.__day = int(day)
        self.__month = int(month)
        self.__year = int(year)

    @property
    def day(self) -> int:
        return self.__day

    @property
    def month(self) -> int:
        return self.__month

    @property
    def year(self) -> int:
        return self.__year

    def to_iso(self) -> str:
        return f"{self.__year:04d}-{self.__month:02d}-{self.__day:02d}"

    @classmethod
    def from_iso(cls, iso: str) -> "Date":
        parts = iso.split("-")
        if len(parts) != 3:
            raise ValueError("Формат даты должен быть YYYY-MM-DD")
        y, m, d = map(int, parts)
        return cls(d, m, y)

    def to_stddate(self) -> _date:
        return _date(self.__year, self.__month, self.__day)

    @classmethod
    def today(cls) -> "Date":
        td = _date.today()
        return cls(td.day, td.month, td.year)

    def __eq__(self, other) -> bool:
        return isinstance(other, Date) and (self.__year, self.__month, self.__day) == (other.__year, other.__month, other.__day)

    def __lt__(self, other) -> bool:
        if not isinstance(other, Date):
            return NotImplemented
        return (self.__year, self.__month, self.__day) < (other.__year, other.__month, other.__day)

    def __le__(self, other) -> bool:
        if not isinstance(other, Date):
            return NotImplemented
        return self == other or self < other

    def __repr__(self) -> str:
        return f"Date({self.to_iso()})"
