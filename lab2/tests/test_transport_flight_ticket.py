import pytest
from src.products.Transport import Transport
from src.products.Flight import Flight
from src.products.Ticket import Ticket
from src.techs.Date import Date
from src.exceptions.exceptions import TransportDelayException

def test_transport_and_capacity():
    tr = Transport("bus", 20)
    assert tr.capacity() == 20
    r = type("R", (), {"id":"rid"})()
    tr.assign_route(r)
    assert getattr(tr, "_Transport__route") is r

def test_flight_reschedule_and_ticket():
    f = Flight("FL1", Date(10,10,2025))
    t = Ticket("T1", Date(10,10,2025))
    t.assign_flight(f)
    with pytest.raises(ValueError):
        f.reschedule(Date(1,1,2025))  # earlier
    f.reschedule(Date(11,10,2025))
    t.change_date(Date(12,10,2025))
