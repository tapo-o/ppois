from uuid import uuid4
from src.employers.Client import Client
from src.products.Tour import Tour
from src.products.Hotel import Hotel
from src.products.Room import Room
from src.finance.BankCard import BankCard
from src.techs.Date import Date

class Factory:
    @staticmethod
    def make_client(name: str, email: str) -> Client:
        return Client(name, email)

    @staticmethod
    def make_tour(title: str, price: float) -> Tour:
        return Tour(title, price)

    @staticmethod
    def make_hotel(name: str, address: str) -> Hotel:
        return Hotel(name, address)

    @staticmethod
    def make_room(room_type: str, price: float) -> Room:
        return Room(room_type, price)

    @staticmethod
    def make_card(number: str, balance: float, expiry_iso: str, pin: str) -> BankCard:
        d = Date.from_iso(expiry_iso)
        return BankCard(number, balance, d, pin)

