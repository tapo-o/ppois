import pytest
from src.products.TourCatalog import TourCatalog
from src.products.TourSearch import TourSearch
from src.products.Tour import Tour
from src.finance.Discount import Discount
from src.finance.PromoCode import PromoCode
from src.techs.Date import Date
from src.exceptions.exceptions import TourNotFoundException, BookingAlreadyExistsException

def test_catalog_and_search():
    cat = TourCatalog("All")
    t1 = Tour("A", 50.0)
    t2 = Tour("B", 200.0)
    cat.add_tour(t1); cat.add_tour(t2)
    ts = TourSearch()
    res = ts.find_by_price(cat, 40, 100)
    assert any(getattr(x, "_Tour__title", "") == "A" for x in res)
    with pytest.raises(TourNotFoundException):
        ts.find_by_price(cat, 1000, 2000)

def test_discount_and_promo():
    d = Discount("D1", 10.0)
    t = Tour("T", 150.0)
    class C: 
        def __init__(self): self.__cards = [1]
        def get_cards(self): return self.__cards
    c = C()
    assert d.is_applicable(c, t)
    assert d.calculate(200.0) == 20.0
    promo = PromoCode("P1", 20.0, Date(1,1,2099))
    # activate for fake client
    fake = type("F", (), {"id":"cid"})()
    promo.activate_for(fake)
    with pytest.raises(BookingAlreadyExistsException):
        promo.activate_for(fake)
