'''Test cases for Calculator class'''
from decimal import Decimal
import pytest
from calculator.calculator import Calculator

@pytest.mark.parametrize("operand_a, operand_b, expected", [
    (Decimal('3'), Decimal('4'), Decimal('7')),
    (Decimal('3.4'), Decimal('4.2'), Decimal('7.6')),
    (Decimal('0'), Decimal('4'), Decimal('4')),
    (Decimal('3'), Decimal('0'), Decimal('3')),
])
def test_operation_add(operand_a, operand_b, expected):
    '''test add method in calculator class'''
    assert Calculator.add(operand_a, operand_b) == expected
    assert Calculator.add(operand_b, operand_a) == expected


@pytest.mark.parametrize("operand_a, operand_b, expected", [
    (Decimal('4'), Decimal('3'), Decimal('1')),
    (Decimal('3'), Decimal('3'), Decimal('0')),
    (Decimal('2'), Decimal('4'), Decimal('-2')),
    (Decimal('7.2'), Decimal('4.1'), Decimal('3.1')),
])
def test_operation_subtract(operand_a, operand_b, expected):
    '''test subtract method in calculator class'''
    assert Calculator.subtract(operand_a, operand_b) == expected

@pytest.mark.parametrize("operand_a, operand_b, expected", [
    (Decimal('3'), Decimal('4'), Decimal('12')),
    (Decimal('3.4'), Decimal('4.8'), Decimal('16.32')),
    (Decimal('0'), Decimal('4'), Decimal('0')),
    (Decimal('3'), Decimal('-4'), Decimal('-12')),
])
def test_operation_multiply(operand_a, operand_b, expected):
    '''test multiply method in calculator class'''
    assert Calculator.multiply(operand_a, operand_b) == expected
    assert Calculator.multiply(operand_b, operand_a) == expected

@pytest.mark.parametrize("operand_a, operand_b, expected", [
    (Decimal('12'), Decimal('4'), Decimal('3')),
    (Decimal('0'), Decimal('4'), Decimal('0')),
    (Decimal('3.8'), Decimal('2'), Decimal('1.9')),
])
def test_operation_division(operand_a, operand_b, expected):
    '''test division method in calculator class'''
    assert Calculator.division(operand_a, operand_b) == expected
