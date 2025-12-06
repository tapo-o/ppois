from src.employers.Employee import Employee
from src.exceptions.exceptions import TourNotFoundException
from typing import List

class BookingAgent(Employee):
    def __init__(self, name: str):
        super().__init__(name, "booking_agent")
        self.__rating = 0.0
        self.__managed_clients: List[str] = []

    #бронь и управление
    def create_booking(self, client, tour) -> None:
        client.book_tour(tour)
        if client.id not in self.__managed_clients:
            self.__managed_clients.append(client.id)

    #отмена брони
    def cancel_booking(self, client, tour) -> None:
        if tour.id not in client.get_bookings():
            raise TourNotFoundException("Бронь не найдена")

    #добавляет клиента в список управяемых
    def take_over_client(self, client) -> None:
        if client.id not in self.__managed_clients:
            self.__managed_clients.append(client.id)

    def get_managed(self) -> List[str]:
        return list(self.__managed_clients)
