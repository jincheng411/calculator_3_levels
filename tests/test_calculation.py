'''Test cases for Calculation class'''
from calculator.operations import Operations
from calculator.calculation import Calculation

def test_calculation_operations():
    '''Test perform method'''
    cal = Calculation(1, 2, Operations.add)
    assert cal.perform() == 3
