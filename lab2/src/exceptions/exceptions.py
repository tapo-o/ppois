# exceptions.py
class InvalidPasswordException(Exception):
    """Неверный пароль или пин-код."""
    pass

class InsufficientFundsException(Exception):
    """Недостаточно средств для операции."""
    pass

class TourNotFoundException(Exception):
    """Тур не найден."""
    pass

class HotelNotAvailableException(Exception):
    """Отель/номер недоступен на выбранные даты."""
    pass

class BookingAlreadyExistsException(Exception):
    """Бронирование уже существует."""
    pass

class CardExpiredException(Exception):
    """Срок действия карты истёк."""
    pass

class InvalidEmailException(Exception):
    """Неверный формат email."""
    pass

class UnauthorizedAccessException(Exception):
    """Недостаточный уровень доступа."""
    pass

class PaymentFailedException(Exception):
    """Платёж не прошёл."""
    pass

class GuideNotFoundException(Exception):
    """Гид недоступен или не найден."""
    pass

class TransportDelayException(Exception):
    """Задержка транспорта/неисправность."""
    pass

class ContractViolationException(Exception):
    """Нарушение условий договора/операции."""
    pass

# Явный список для from exceptions import *
__all__ = [
    "InvalidPasswordException",
    "InsufficientFundsException",
    "TourNotFoundException",
    "HotelNotAvailableException",
    "BookingAlreadyExistsException",
    "CardExpiredException",
    "InvalidEmailException",
    "UnauthorizedAccessException",
    "PaymentFailedException",
    "GuideNotFoundException",
    "TransportDelayException",
    "ContractViolationException",
]
