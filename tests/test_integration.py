from src.calculator import add, divide
import pytest

def test_full_flow():
    result = divide(add(10, 5), 3)
    assert result == 5