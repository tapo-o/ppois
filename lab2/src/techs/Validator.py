from typing import Any
from src.exceptions.exceptions import InvalidEmailException

class Validator:
    @staticmethod
    def validate_email(email: str) -> None:
        if not isinstance(email, str) or "@" not in email or "." not in email:
            raise InvalidEmailException(f"Неверный email: {email}")

    @staticmethod
    def validate_nonempty_str(value: Any, name: str) -> None:
        if not isinstance(value, str) or not value.strip():
            raise ValueError(f"{name} должен быть непустой строкой")

    @staticmethod
    def validate_positive_number(value: Any, name: str) -> None:
        try:
            v = float(value)
        except Exception:
            raise ValueError(f"{name} должен быть числом")
        if v <= 0:
            raise ValueError(f"{name} должен быть положительным")
