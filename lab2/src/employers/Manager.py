from src.employers.Employee import Employee
from src.exceptions.exceptions import TourNotFoundException
from typing import Optional

class Manager(Employee):
    def __init__(self, name: str):
        super().__init__(name, "manager")
        self.__department_id: Optional[str] = None

    @property
    def department_id(self) -> Optional[str]:
        return self.__department_id

    def _assign_department(self, dep_id: str) -> None:
        self.__department_id = dep_id

    # Подтверждает бронь: проверяет, что у клиента есть указанная бронь, иначе бросает исключение
    def approve_booking(self, tour, client) -> None:
        if tour.id not in client.get_bookings():
            raise TourNotFoundException("У клиента нет такого бронирования")

    # Переназначает клиента другому агенту, вызывая у агента метод взятия клиента под управление
    def reassign_client(self, client, agent) -> None:
        agent.take_over_client(client)
