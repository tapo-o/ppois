import pytest
from src.finance.BankCard import BankCard
from src.finance.PaymentSystem import PaymentSystem
from src.finance.Payment import Payment
from src.finance.Invoice import Invoice
from src.techs.Date import Date
from src.exceptions.exceptions import InsufficientFundsException, InvalidPasswordException, PaymentFailedException

def test_bankcard_transfer_and_pin():
    c1 = BankCard("1111", 100.0, Date(31,12,2099), "1234")
    c2 = BankCard("2222", 0.0, Date(31,12,2099), "0000")
    with pytest.raises(InvalidPasswordException):
        c1.check_pin("0000")
    assert c1.check_pin("1234")
    c1.transfer_to(c2, 50.0, "1234")
    assert c1.balance() == 50.0
    assert c2.balance() == 50.0
    with pytest.raises(InsufficientFundsException):
        c1.transfer_to(c2, 100.0, "1234")

def test_payment_system_process(monkeypatch):
    ps = PaymentSystem("prov", 1.0)
    p = Payment(10.0)
    c = BankCard("1111", 100.0, Date(31,12,2099), "1234")
    # execute should set status to PAID
    p.execute(ps, c, "1234")
    assert p.status() == "PAID"

def test_invoice_generate_send():
    from src.employers.Client import Client
    from src.products.Tour import Tour
    client = Client("A", "a@a.com")
    tour = Tour("X", 100.0)
    inv = Invoice()
    inv.generate(client, tour)
    assert inv.amount() == 100.0
    inv.send()
    with pytest.raises(Exception):
        inv.send()  # already sent raises BookingAlreadyExistsException

def test_bankcard_transfer_success_and_balance_update():
    c1 = BankCard("1111", 200.0, Date(31,12,2099), "1234")
    c2 = BankCard("2222", 50.0, Date(31,12,2099), "0000")
    # успешный перевод уменьшает баланс отправителя и увеличивает получателя
    c1.transfer_to(c2, 75.0, "1234")
    assert c1.balance() == pytest.approx(125.0)
    assert c2.balance() == pytest.approx(125.0)

def test_bankcard_transfer_invalid_pin_raises():
    c1 = BankCard("3333", 100.0, Date(31,12,2099), "9999")
    c2 = BankCard("4444", 0.0, Date(31,12,2099), "0000")
    with pytest.raises(Exception):
        c1.transfer_to(c2, 10.0, "0000")

def test_payment_system_process_success_changes_payment_status():
    ps = PaymentSystem("provider-x", 2.5)  # комиссия 2.5%
    p = Payment(40.0)
    client_card = BankCard("5555", 100.0, Date(31,12,2099), "4321")
    system_card = BankCard("SYS-1", 0.0, Date(31,12,2099), "0000")
    # process_payment должен перевести сумму с комиссией и пометить платёж PAID
    ps.process_payment(p, client_card, "4321", system_wallet=system_card)
    assert p.status() == "PAID"
    # проверяем, что системный кошелёк получил сумму с комиссией
    total = 40.0 * (1.0 + 2.5 / 100.0)
    assert system_card.balance() == pytest.approx(total)

def test_payment_execute_sets_failed_on_exception(monkeypatch):
    ps = PaymentSystem("prov", 0.0)
    p = Payment(10.0)
    # создаём карту, чей transfer_to бросает исключение
    class FaultyCard:
        def transfer_to(self, other, amount, pin):
            raise Exception("network error")
    bad = FaultyCard()
    with pytest.raises(Exception):
        p.execute(ps, bad, "0000")
    # статус должен быть обновлён в FAILED
    assert p.status() == "FAILED"

