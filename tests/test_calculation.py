from decimal import Decimal
from calculator import add, subtract
from calculator.calculation import Calculation
import pytest

def test_calculation_operations():
    cal = Calculation(Decimal('1'), Decimal('2'), add)
    assert cal.perform() == Decimal('3'), f"calculation add method failed"