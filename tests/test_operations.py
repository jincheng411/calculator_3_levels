'''My operations Test'''
from calculator.operations import Operations
def test_addition():
    '''Test that addition function works '''
    assert Operations.add(2,2) == 4

def test_subtraction():
    '''Test that subtraction function works '''
    assert Operations.subtract(2,2) == 0

def test_multiplication():
    '''Test that multiply function works '''
    assert Operations.multiply(2,3) == 6

def test_division():
    '''Test that division function works '''
    assert Operations.division(6,2) == 3
