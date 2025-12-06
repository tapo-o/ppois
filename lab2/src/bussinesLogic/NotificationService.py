from src.techs.Validator import Validator
from src.exceptions.exceptions import UnauthorizedAccessException, InvalidEmailException

class NotificationService:
    def __init__(self, channel: str, priority: str = "normal"):
        Validator.validate_nonempty_str(channel, "channel")
        self.__channel = channel
        self.__priority = priority
        self.__enabled = True
        self.__log: list = []

    def enable(self) -> None:
        self.__enabled = True

    def disable(self) -> None:
        self.__enabled = False

    def send_sms(self, number: str, text: str) -> None:
        if not self.__enabled or self.__channel != "sms":
            raise UnauthorizedAccessException("Канал SMS недоступен")
        if not isinstance(number, str) or len(number) < 7:
            raise ValueError("Некорректный номер")
        self.__log.append(("sms", number, text))

    def send_email(self, email: str, subject: str, text: str) -> None:
        if not self.__enabled or self.__channel != "email":
            raise UnauthorizedAccessException("Канал email недоступен")
        try:
            Validator.validate_email(email)
        except InvalidEmailException:
            raise
        self.__log.append(("email", email, subject, text))

    def sent_count(self) -> int:
        return len(self.__log)

