from uuid import uuid4
from typing import List, Dict
from src.techs.Validator import Validator

class AuditLog:
    def __init__(self):
        self.__id = str(uuid4())
        self.__records: List[Dict[str, str]] = []

    # Добавляет запись в журнал после валидации входных данных
    def write(self, actor_id: str, role: str, description: str) -> None:
        Validator.validate_nonempty_str(actor_id, "actor_id")
        Validator.validate_nonempty_str(role, "role")
        Validator.validate_nonempty_str(description, "description")
        self.__records.append({
            "actor_id": actor_id,
            "role": role,
            "description": description,
            "time": "2025-01-01T00:00:00"  # упрощённо
        })

    def get_by_actor(self, actor_id: str) -> List[Dict[str, str]]:
        return [r for r in self.__records if r["actor_id"] == actor_id]

    def all(self) -> List[Dict[str, str]]:
        return list(self.__records)
