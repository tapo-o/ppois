from uuid import uuid4
from typing import Optional
from src.techs.Validator import Validator
from src.exceptions.exceptions import UnauthorizedAccessException

class Authorization:

    def __init__(self):
        self.__token: Optional[str] = None
        self.__level: int = 0
        self.__user_email: Optional[str] = None

    # минимальная валидация входных данных
    def login(self, email: str, password: str, required_level: int = 1) -> str:
        Validator.validate_nonempty_str(email, "email")
        Validator.validate_nonempty_str(password, "password")
        if required_level < 0:
            raise ValueError("required_level должен быть неотрицательным")
        
        token = str(uuid4())
        self.__token = token
        self.__level = int(required_level)
        self.__user_email = email
        return token

    def token(self) -> Optional[str]:
        return self.__token

    def logout(self) -> None:
        self.__token = None
        self.__level = 0
        self.__user_email = None

    #Проверяет, что текущий пользователь авторизован и имеет уровень >= required_level. Бросает UnauthorizedAccessException в противном случае.
    def check_access(self, required_level: int) -> None:
        if self.__token is None:
            raise UnauthorizedAccessException("Нет активной сессии")
        if required_level < 0:
            raise ValueError("required_level должен быть неотрицательным")
        if self.__level < required_level:
            raise UnauthorizedAccessException("Недостаточный уровень доступа")
