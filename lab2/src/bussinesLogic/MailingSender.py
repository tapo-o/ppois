from uuid import uuid4
from src.techs.Validator import Validator
from src.bussinesLogic.NotificationService import NotificationService

class MailingSender:
    def __init__(self, subject: str, body: str):
        Validator.validate_nonempty_str(subject, "subject")
        Validator.validate_nonempty_str(body, "body")
        self.__id = str(uuid4())
        self.__subject = subject
        self.__body = body
        self.__recipients = []

    def add_recipient(self, email: str) -> None:
        Validator.validate_nonempty_str(email, "email")
        self.__recipients.append(email)

    def send_all(self, notification: NotificationService) -> int:
        sent = 0
        for e in list(self.__recipients):
            try:
                notification.send_email(e, self.__subject, self.__body)
                sent += 1
            except Exception:
                continue
        return sent
