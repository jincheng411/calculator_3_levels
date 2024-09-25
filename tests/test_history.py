from typing import List
import pytest
from calculator.calculation import Calculation
from calculator.history import History
from calculator.operations import Operations


def test_add_calculation():
    cal1 = Calculation.create(1 , 2, Operations.add)
    cal2 = Calculation.create(3 , 4, Operations.multiply)
    History.add_calculation(cal1)
    History.add_calculation(cal2)
    assert len(History.history) == 2
    assert isinstance(History.history[0], Calculation)
    assert isinstance(History.history[1], Calculation)

def test_get_history():
    assert len(History.get_history()) == 2

def test_print_history():
    assert History.print_history() == "1. calculation: 1, 2, add. 2. calculation: 3, 4, multiply. "

def test_clear_history():
    assert len(History.get_history()) == 2
    History.clear_history()
    assert len(History.get_history()) == 0