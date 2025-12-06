from uuid import uuid4
from src.techs.Validator import Validator
from src.exceptions.exceptions import InvalidPasswordException

class Employee:
    def __init__(self, name: str, role: str):
        Validator.validate_nonempty_str(name, "name")
        Validator.validate_nonempty_str(role, "role")
        self.__id = str(uuid4())
        self.__name = name
        self.__role = role
        self.__password = ""

    @property
    def id(self) -> str:
        return self.__id

    @property
    def name(self) -> str:
        return self.__name

    @property
    def role(self) -> str:
        return self.__role

    # Устанавливает пароль после проверки минимальной длины
    def set_password(self, password: str) -> None:
        if not isinstance(password, str) or len(password) < 4:
            raise InvalidPasswordException("Пароль слишком короткий")
        self.__password = password

    # Проверяет соответствие пароля и бросает исключение при несоответствии
    def check_password(self, password: str) -> bool:
        if self.__password != password:
            raise InvalidPasswordException("Неверный пароль")
        return True

    # Внутренний метод для изменения роли сотрудника
    def _set_role(self, role: str) -> None:
        self.__role = role
