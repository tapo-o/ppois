from src.employers.Employee import Employee
from src.exceptions.exceptions import GuideNotFoundException
from typing import List

class Guide(Employee):
    def __init__(self, name: str, languages: List[str]):
        super().__init__(name, "guide")
        self.__languages = list(languages)

    @property
    def languages(self) -> List[str]:
        return list(self.__languages)

    # Назначает гида на экскурсию, если у него есть хотя бы один язык, иначе бросает исключение
    def assign_excursion(self, excursion) -> None:
        if not self.__languages:
            raise GuideNotFoundException("Гид не владеет языками")
        excursion.set_guide_id(self.id)

    # Подтверждает доступность гида для маршрута (True, если маршрут задан)
    def confirm_availability(self, route) -> bool:
        return route is not None
