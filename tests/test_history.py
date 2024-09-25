'''Test cases for History class'''
import pytest
from calculator.calculation import Calculation
from calculator.history import History
from calculator.operations import Operations

@pytest.fixture(scope='session', autouse=True)
def clear_calculations_history():
    '''clear histroy before run the test cases'''
    History.history.clear()

def test_add_calculation():
    '''test add calculation history'''
    cal1 = Calculation.create(1, 2, Operations.add)
    cal2 = Calculation.create(3, 4, Operations.multiply)
    History.add_calculation(cal1)
    History.add_calculation(cal2)
    assert len(History.history) == 2
    assert isinstance(History.history[0], Calculation)
    assert isinstance(History.history[1], Calculation)

def test_get_history():
    '''test get history should return calculation objects'''
    assert len(History.get_history()) == 2
    assert isinstance(History.get_history()[0], Calculation)

def test_print_history():
    '''should print the string of calculation of history'''
    assert History.print_history() == "1. calculation: 1, 2, add. 2. calculation: 3, 4, multiply. "

def test_clear_history():
    '''should clear all the calculation history'''
    assert len(History.get_history()) == 2
    History.clear_history()
    assert len(History.get_history()) == 0

def test_get_last_record():
    '''should return the last calculation history'''
    cal = Calculation.create(5, 6, Operations.add)
    History.add_calculation(cal)
    assert History.get_last_record().a == 5
    assert History.get_last_record().b == 6
