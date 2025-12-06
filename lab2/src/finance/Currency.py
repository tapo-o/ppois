from src.techs.Validator import Validator

class Currency:
    def __init__(self, code: str, name: str, rate_to_base: float):
        Validator.validate_nonempty_str(code, "code")
        Validator.validate_nonempty_str(name, "name")
        if rate_to_base <= 0:
            raise ValueError("rate_to_base должен быть положительным")
        self.__code = code
        self.__name = name
        self.__rate_to_base = float(rate_to_base)

    def code(self) -> str:
        return self.__code

    def convert_to(self, amount: float, target: "Currency") -> float:
        if amount < 0:
            raise ValueError("amount не может быть отрицательным")
        base = amount * self.__rate_to_base
        return base / target.__rate_to_base

    def update_rate(self, new_rate: float) -> None:
        if new_rate <= 0:
            raise ValueError("new_rate должен быть положительным")
        self.__rate_to_base = float(new_rate)
