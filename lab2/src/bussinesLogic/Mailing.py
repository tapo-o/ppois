from uuid import uuid4
from typing import List
from src.techs.Validator import Validator
from src.bussinesLogic.NotificationService import NotificationService

class Mailing:
    def __init__(self, subject: str, body: str):
        Validator.validate_nonempty_str(subject, "subject")
        Validator.validate_nonempty_str(body, "body")
        self.__id = str(uuid4())
        self.__subject = subject
        self.__body = body
        self.__recipients: List[str] = []
        self.__status = "NEW"

    def add_recipient(self, email: str) -> None:
        Validator.validate_nonempty_str(email, "email")
        self.__recipients.append(email)

    def send(self, notification: NotificationService) -> None:
        for e in list(self.__recipients):
            try:
                notification.send_email(e, self.__subject, self.__body)
            except Exception:
                continue
        self.__status = "SENT"

    def status(self) -> str:
        return self.__status
