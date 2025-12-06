import pytest
from src.bussinesLogic.NotificationService import NotificationService
from src.finance.BookingCalendar import BookingCalendar
from src.products.Review import Review
from src.products.HotelRating import HotelRating
from src.products.Hotel import Hotel
from src.techs.Date import Date

def test_notification_email_sms():
    ns = NotificationService("email")
    ns.send_email("a@b.com", "subj", "body")
    assert ns.sent_count() == 1
    ns_sms = NotificationService("sms")
    ns_sms.send_sms("+1234567", "hi")
    assert ns_sms.sent_count() == 1

def test_calendar_and_events():
    cal = BookingCalendar("cal", "UTC")
    class T: pass
    t = T(); t.id = "tid"
    cal.add_event(t, Date(1,1,2025))
    assert cal.has_event("tid")
    cal.remove_event(t)
    assert not cal.has_event("tid")

def test_review_and_rating():
    hotel = Hotel("H", "Addr")
    r = Review("Auth", "Nice")
    r.attach_to_hotel(hotel)
    assert "(есть отзыв)" in hotel._Hotel__name
    hr = HotelRating(4)
    hr.add_review(r)
    avg = hr.recalc_average()
    assert avg <= 4.0
