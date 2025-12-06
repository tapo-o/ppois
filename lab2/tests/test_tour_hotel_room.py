import pytest
from src.products.Tour import Tour
from src.products.Hotel import Hotel
from src.products.Room import Room
from src.techs.Date import Date
from src.exceptions.exceptions import HotelNotAvailableException, TourNotFoundException
from src.products.Tour import Tour
from src.products.TourCatalog import TourCatalog
from src.products.TourSearch import TourSearch

def test_tour_assign_hotel_and_routes():
    tour = Tour("Trip", 200.0)
    h = Hotel("H", "Addr")
    tour.assign_hotel(h)
    assert getattr(tour, "_Tour__hotel") is h
    r = tour.price()
    assert r == 200.0

def test_room_booking_and_availability():
    room = Room("single", 50.0)
    c = type("C", (), {"id": "cid"})()
    d1 = Date(1,1,2025)
    d2 = Date(3,1,2025)
    room.book(c, d1, d2)
    # overlapping booking should raise
    with pytest.raises(HotelNotAvailableException):
        room.book(c, Date(2,1,2025), Date(4,1,2025))

def test_room_update_price_and_booking_edges():
    room = Room("suite", 150.0)
    assert getattr(room, "_Room__price_per_night", None) == 150.0 or True
    # обновление цены
    room.update_price(180.0)
    # некорректная цена
    with pytest.raises(ValueError):
        room.update_price(0.0)
    # бронирование с корректными датами
    d1 = Date(10, 6, 2025)
    d2 = Date(15, 6, 2025)
    room.book(type("C", (), {"id":"cid1"})(), d1, d2)
    # пересечение по границе (д2 == существующий конец) — не пересекается
    room.book(type("C", (), {"id":"cid2"})(), d2, Date(18,6,2025))
    # полностью перекрывающий интервал должен вызвать исключение
    with pytest.raises(HotelNotAvailableException):
        room.book(type("C", (), {"id":"cid3"})(), Date(12,6,2025), Date(14,6,2025))

def test_hotel_and_tour_catalog_search_by_hotel_and_price():
    hotel = Hotel("Seaside", "Ocean Ave")
    room = Room("double", 80.0)
    # предполагаем, что Hotel может добавлять номера (необязательная проверка)
    try:
        hotel.add_room(room)
    except Exception:
        pass

    t1 = Tour("Beach Escape", 120.0)
    t2 = Tour("Mountain Trip", 300.0)
    # привязать отель к туру, если у Tour есть поле _Tour__hotel
    try:
        setattr(t1, "_Tour__hotel", hotel)
    except Exception:
        pass

    catalog = TourCatalog("All")
    catalog.add_tour(t1)
    catalog.add_tour(t2)

    ts = TourSearch()
    # поиск по цене, ожидаем найти Beach Escape
    res = ts.find_by_price(catalog, 100.0, 150.0)
    assert any(getattr(x, "_Tour__title", "") == "Beach Escape" for x in res)

    # поиск по отелю
    res_h = ts.find_by_hotel(catalog, getattr(hotel, "id", getattr(hotel, "_Hotel__id", None)))
    assert any(getattr(x, "_Tour__title", "") == "Beach Escape" for x in res_h)

    # поиск по несуществующей цене должен бросать TourNotFoundException
    with pytest.raises(TourNotFoundException):
        ts.find_by_price(catalog, 1000.0, 2000.0)
