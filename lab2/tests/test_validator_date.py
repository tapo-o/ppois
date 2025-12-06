import pytest
from src.techs.Validator import Validator
from src.techs.Date import Date
from src.exceptions.exceptions import InvalidEmailException

def test_validate_nonempty_str_ok():
    Validator.validate_nonempty_str("hello", "field")

def test_validate_nonempty_str_fail():
    with pytest.raises(ValueError):
        Validator.validate_nonempty_str("", "field")

def test_validate_email_ok():
    Validator.validate_email("a@b.com")

def test_validate_email_fail():
    with pytest.raises(InvalidEmailException):
        Validator.validate_email("not-an-email")

def test_date_iso_and_comparison():
    d = Date(5, 6, 2025)
    assert d.to_iso() == "2025-06-05"
    d2 = Date.from_iso("2025-06-06")
    assert d < d2
    assert d <= d2
    assert not (d2 < d)
