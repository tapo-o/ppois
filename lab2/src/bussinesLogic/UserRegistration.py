from uuid import uuid4
from src.techs.Validator import Validator
from src.exceptions.exceptions import InvalidEmailException, InvalidPasswordException

class UserRegistration:
    def __init__(self, email: str):
        Validator.validate_nonempty_str(email, "email")
        Validator.validate_email(email)
        self.__id = str(uuid4())
        self.__email = email
        self.__registered_at = None 
        self.__confirmed = False

    @property
    def id(self) -> str:
        return self.__id

    def register(self, password: str) -> None:
        if not isinstance(password, str) or len(password) < 6:
            raise InvalidPasswordException("Пароль должен быть не менее 6 символов")
        from src.techs.Date import Date
        self.__registered_at = Date(1, 1, 2025).to_iso()

    def confirm_email(self, code: str) -> None:
        if not isinstance(code, str) or len(code.strip()) == 0:
            raise ValueError("Код подтверждения некорректен")
        self.__confirmed = True

    def is_confirmed(self) -> bool:
        return self.__confirmed

