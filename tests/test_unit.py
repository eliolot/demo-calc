from src.calculator import add, divide, multiply, subtract
import pytest

def test_add():
    assert add(2, 3) == 5

def test_add_negative():
    assert add(-2, -3) == -5

def test_subtract():
    assert subtract(5, 2) == 3

def test_subtract_negative():
    assert subtract(-5, -2) == -3

def test_multiply():
    assert multiply(2, 3) == 6

def test_divide():
    assert divide(10, 2) == 5

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)