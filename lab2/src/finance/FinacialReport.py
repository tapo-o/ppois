from uuid import uuid4
from src.techs.Validator import Validator

class FinancialReport:
    def __init__(self, period: str):
        Validator.validate_nonempty_str(period, "period")
        self.__id = str(uuid4())
        self.__period = period
        self.__total = 0.0

    def collect_data(self, company: object) -> None:
        active = sum(1 for c in getattr(company, "_Company__contracts", {}).values() if getattr(c, "is_active", lambda: False)())
        self.__total = active * 1000.0

    def summarize(self) -> str:
        return f"{self.__period}:{self.__total}"
