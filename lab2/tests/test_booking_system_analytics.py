import pytest
from src.finance.BookingSystem import BookingSystem
from src.bussinesLogic.AnalyticsSystem import AnalyticsSystem
from src.bussinesLogic.Company import Company
from src.bussinesLogic.Contract import Contract
from src.employers.Client import Client
from src.employers.Manager import Manager

def test_booking_system_create_cancel():
    bs = BookingSystem("1.0")
    c = Client("X", "x@x.com")
    t = type("T", (), {"id":"tid"})()
    bs.create_booking(c, t)
    assert bs.is_booked(c.id, t.id)
    bs.cancel_booking(c, t)
    assert not bs.is_booked(c.id, t.id)

def test_analytics_collect():
    comp = Company("Co", "Addr")
    # create contract and sign
    client = Client("C", "c@c.com")
    comp.add_client(client)
    mgr = Manager("M")
    contract = Contract("num")
    contract.sign(client, mgr)
    comp._Company__contracts[contract._Contract__id] = contract
    an = AnalyticsSystem("v", "s")
    metrics = an.collect_metrics(comp)
    assert "clients" in metrics
