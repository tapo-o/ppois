from src.techs.Validator import Validator

class Discount:
    def __init__(self, code: str, percent: float, conditions: str = ""):
        Validator.validate_nonempty_str(code, "code")
        if not (0 < percent <= 100):
            raise ValueError("percent должен быть в диапазоне (0,100]")
        self.__code = code
        self.__percent = float(percent)
        self.__conditions = conditions

    def id(self) -> str:
        return self.__code

    # Вычисляет сумму скидки от базовой суммы
    def calculate(self, base_amount: float) -> float:
        if base_amount < 0:
            raise ValueError("base_amount не может быть отрицательным")
        return base_amount * (self.__percent / 100.0)

    # Проверяет применимость скидки
    def is_applicable(self, client: object, tour: object) -> bool:
        try:
            has_card = len(client.get_cards()) > 0
            price = getattr(tour, "_Tour__price", 0.0)
            return has_card and price > 0
        except Exception:
            return False
