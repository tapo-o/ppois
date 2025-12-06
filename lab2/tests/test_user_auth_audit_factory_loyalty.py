import pytest
from src.bussinesLogic.UserRegistration import UserRegistration
from src.bussinesLogic.Authorization import Authorization
from src.bussinesLogic.Auditlog import AuditLog
from src.bussinesLogic.Factory import Factory
from src.products.LoyaltyProgram import LoyaltyProgram
from src.employers.Client import Client

def test_user_registration_and_confirm():
    ur = UserRegistration("u@u.com")
    ur.register("password")
    assert not ur.is_confirmed()
    ur.confirm_email("CODE")
    assert ur.is_confirmed()

def test_authorization_token_and_access():
    auth = Authorization()
    token = auth.login("a@a.com", "pwd", required_level=2)
    assert auth.token() == token
    with pytest.raises(Exception):
        auth.check_access(3)  # insufficient

def test_audit_log_write_and_get():
    al = AuditLog()
    al.write("actor1", "role", "did something")
    recs = al.get_by_actor("actor1")
    assert len(recs) == 1

def test_factory_and_loyalty():
    f = Factory()
    c = f.make_client("Name", "n@e.com")
    assert isinstance(c, Client)
    lp = LoyaltyProgram("LP")
    lp.enroll(c.id)
    lp.add_points(c.id, 10.0)
    assert lp.get_balance(c.id) == 10.0

def test_user_registration_register_invalid_password():
    ur = UserRegistration("v@v.com")
    # короткий пароль должен вызвать исключение при регистрации
    with pytest.raises(Exception):
        ur.register("123")  # ожидаем ошибку валидации пароля

def test_authorization_logout_and_token_none():
    auth = Authorization()
    token = auth.login("b@b.com", "secret", required_level=1)
    assert auth.token() == token
    auth.logout()
    assert auth.token() is None
    # после logout доступ должен быть запрещён для требуемого уровня
    with pytest.raises(Exception):
        auth.check_access(1)

def test_audit_log_all_and_get_by_actor():
    al = AuditLog()
    al.write("actorX", "roleX", "action1")
    al.write("actorY", "roleY", "action2")
    all_records = al.all()
    assert isinstance(all_records, list) and len(all_records) >= 2
    recs_x = al.get_by_actor("actorX")
    assert any(r["actor_id"] == "actorX" for r in recs_x)

def test_factory_maketers_and_client_type():
    f = Factory()
    c = f.make_client("Name2", "n2@e.com")
    assert isinstance(c, Client)
    # фабрика должна создавать объекты с ожидаемыми атрибутами
    t = f.make_tour("Title", 77.0)
    assert getattr(t, "_Tour__title", None) == "Title"
    h = f.make_hotel("HName", "Addr")
    assert getattr(h, "_Hotel__name", None) == "HName"

def test_loyalty_enroll_and_points_edge_cases():
    lp = LoyaltyProgram("Gold")
    cid = "client-xyz"
    # повторная регистрация не должна ломать
    lp.enroll(cid)
    lp.enroll(cid)
    # добавление нулевых/отрицательных очков — ошибка
    with pytest.raises(Exception):
        lp.add_points(cid, -1.0)
    with pytest.raises(Exception):
        lp.add_points(cid, 0.0)
    # корректное добавление
    lp.add_points(cid, 5.0)
    assert lp.get_balance(cid) == 5.0
