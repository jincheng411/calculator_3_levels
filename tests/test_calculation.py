'''Test cases for Calculation class'''
from decimal import Decimal
import pytest
from calculator.operations import add, subtract, multiply, division
from calculator.calculation import Calculation

# @pytest.mark.parametrize("operand_a, operand_b, operation, expected", [
#     (Decimal('3'), Decimal('4'), Operations.add, Decimal('7')),
#     (Decimal('3.4'), Decimal('4.2'), Operations.add, Decimal('7.6')),
#     (Decimal('0'), Decimal('4'), Operations.add, Decimal('4')),
#     (Decimal('3'), Decimal('0'), Operations.add, Decimal('3')),
#     (Decimal('4'), Decimal('3'), Operations.subtract, Decimal('1')),
#     (Decimal('3'), Decimal('3'), Operations.subtract, Decimal('0')),
#     (Decimal('2'), Decimal('4'), Operations.subtract, Decimal('-2')),
#     (Decimal('7.2'), Decimal('4.1'), Operations.subtract, Decimal('3.1')),
#     (Decimal('3'), Decimal('4'), Operations.multiply, Decimal('12')),
#     (Decimal('3.4'), Decimal('4.8'), Operations.multiply, Decimal('16.32')),
#     (Decimal('0'), Decimal('4'), Operations.multiply, Decimal('0')),
#     (Decimal('3'), Decimal('-4'), Operations.multiply, Decimal('-12')),
#     (Decimal('12'), Decimal('4'), Operations.division, Decimal('3')),
#     (Decimal('0'), Decimal('4'), Operations.division, Decimal('0')),
#     (Decimal('3.8'), Decimal('2'), Operations.division, Decimal('1.9')),
# ])
def test_calculation_operations(operand_a, operand_b, operation, expected):
    '''Test perform method'''
    cal = Calculation(operand_a, operand_b, operation)
    assert cal.perform() == expected

def test_create_calculation():
    '''Test create calculation use factory'''
    cal = Calculation.create(2, 3, division)
    assert isinstance(cal, Calculation)

def test_division_by_zero_exception():
    '''Test should throw an exception if divide by zero'''
    cal = Calculation(0, 0, division)
    with pytest.raises(ZeroDivisionError):
        cal.perform()
