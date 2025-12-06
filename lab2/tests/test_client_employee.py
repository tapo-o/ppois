import pytest
from src.employers.Client import Client
from src.employers.Employee import Employee
from src.employers.Manager import Manager
from src.employers.BookingAgent import BookingAgent
from src.exceptions.exceptions import BookingAlreadyExistsException, InvalidPasswordException

def test_client_attach_and_book():
    c = Client("Ivan", "ivan@example.com")
    assert c.name == "Ivan"
    # create a minimal fake tour with id attribute
    class T: pass
    t = T(); t.id = "tour-1"
    c.book_tour(t)
    assert "tour-1" in c.get_bookings()
    with pytest.raises(BookingAlreadyExistsException):
        c.book_tour(t)

def test_employee_password():
    e = Employee("Bob", "role")
    with pytest.raises(InvalidPasswordException):
        e.set_password("a")
    e.set_password("abcd")
    assert e.check_password("abcd")
    with pytest.raises(InvalidPasswordException):
        e.check_password("wrong")

def test_manager_reassign_and_approve():
    m = Manager("Masha")
    agent = BookingAgent("Agent")
    c = Client("Client", "c@c.com")
    class T: pass
    t = T(); t.id = "t1"
    c.book_tour(t)
    # approve should not raise
    m.approve_booking(t, c)
    # reassign
    m.reassign_client(c, agent)
    assert c.id in agent.get_managed()
