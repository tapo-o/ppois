from src.employers.Employee import Employee
from src.exceptions.exceptions import UnauthorizedAccessException
from typing import Any

class Admin(Employee):
    def __init__(self, name: str, level: int = 3):
        super().__init__(name, "admin")
        self.__access_level = int(level)

    @property
    def access_level(self) -> int:
        return self.__access_level

    #блокает юзера при недостаточном уровне доступа или бросает ошибку
    def block_user(self, client) -> None:
        if self.__access_level < 3:
            raise UnauthorizedAccessException("Недостаточный уровень доступа")
        client._mark_blocked()

    #присваивает роль
    def assign_role(self, employee: Any, role: str) -> None:
        if self.__access_level < 4:
            raise UnauthorizedAccessException("Недостаточный уровень доступа")
        employee._set_role(role)
