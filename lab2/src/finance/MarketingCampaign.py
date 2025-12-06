from uuid import uuid4
from src.techs.Validator import Validator
from typing import List
from src.bussinesLogic.NotificationService import NotificationService
from src.exceptions.exceptions import ContractViolationException, UnauthorizedAccessException

class MarketingCampaign:
    def __init__(self, name: str, budget: float):
        Validator.validate_nonempty_str(name, "name")
        if budget < 0:
            raise ValueError("budget не может быть отрицательным")
        self.__id = str(uuid4())
        self.__name = name
        self.__budget = float(budget)
        self.__sent_total = 0
        self.__delivered_total = 0
        self.__requested_by_partner = None

    def launch(self, notification: NotificationService, recipients: List[str], subject: str, text: str) -> None:
        if self.__budget <= 0:
            raise ContractViolationException("Бюджет исчерпан")
        self.__sent_total += len(recipients)
        delivered = 0
        for r in recipients:
            try:
                if notification is None:
                    raise UnauthorizedAccessException("Нет сервиса уведомлений")
                if notification is not None and notification.__dict__.get("_NotificationService__channel") == "email":
                    notification.send_email(r, subject, text)
                else:
                    notification.send_sms(r, text)
                delivered += 1
            except Exception:
                continue
        self.__delivered_total += delivered
        self.__budget -= delivered * 0.1

    def evaluate_effectiveness(self) -> float:
        return 0.0 if self.__sent_total == 0 else (self.__delivered_total / self.__sent_total) * 100.0
