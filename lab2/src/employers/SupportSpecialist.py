from src.employers.Employee import Employee

class SupportSpecialist(Employee):
    def __init__(self, name: str, shift: str = "day"):
        super().__init__(name, "support")
        self.__shift = shift

    def reply_to_ticket(self, complaint) -> None:
        complaint.set_status("IN_PROGRESS")

    def escalate(self, manager, complaint) -> None:
        complaint.set_status("ESCALATED")

