from decimal import Decimal
import pytest

from calculator.calculator import Calculator
from calculator.history import History
from calculator.operations import Operations

@pytest.fixture(scope='session', autouse=True)
def clear_calculations_history():
    History.history.clear()

@pytest.mark.parametrize("operand_a, operand_b, operation, expected", [
    (Decimal('3'), Decimal('4'), Operations.add, Decimal('7')),
    (Decimal('3.4'), Decimal('4.2'), Operations.add, Decimal('7.6')),
    (Decimal('0'), Decimal('4'), Operations.add, Decimal('4')),
    (Decimal('3'), Decimal('0'), Operations.add, Decimal('3')),
    (Decimal('4'), Decimal('3'), Operations.subtract, Decimal('1')),
    (Decimal('3'), Decimal('3'), Operations.subtract, Decimal('0')),
    (Decimal('2'), Decimal('4'), Operations.subtract, Decimal('-2')),
    (Decimal('7.2'), Decimal('4.1'), Operations.subtract, Decimal('3.1')),
    (Decimal('3'), Decimal('4'), Operations.multiply, Decimal('12')),
    (Decimal('3.4'), Decimal('4.8'), Operations.multiply, Decimal('16.32')),
    (Decimal('0'), Decimal('4'), Operations.multiply, Decimal('0')),
    (Decimal('3'), Decimal('-4'), Operations.multiply, Decimal('-12')),
    (Decimal('12'), Decimal('4'), Operations.division, Decimal('3')),
    (Decimal('0'), Decimal('4'), Operations.division, Decimal('0')),
    (Decimal('3.8'), Decimal('2'), Operations.division, Decimal('1.9')),
])
def test_perform_calculation(operand_a, operand_b, operation, expected):
    assert Calculator._perform_operation(operand_a, operand_b, operation) == expected

@pytest.mark.parametrize("operand_a, operand_b, expected", [
    (Decimal('3'), Decimal('4'), Decimal('7')),
    (Decimal('3.4'), Decimal('4.2'), Decimal('7.6')),
    (Decimal('0'), Decimal('4'), Decimal('4')),
    (Decimal('3'), Decimal('0'), Decimal('3')),
])
def test_operation_add(operand_a, operand_b, expected):
    assert Calculator.add(operand_a, operand_b) == expected
    assert Calculator.add(operand_b, operand_a) == expected


@pytest.mark.parametrize("operand_a, operand_b, expected", [
    (Decimal('4'), Decimal('3'), Decimal('1')),
    (Decimal('3'), Decimal('3'), Decimal('0')),
    (Decimal('2'), Decimal('4'), Decimal('-2')),
    (Decimal('7.2'), Decimal('4.1'), Decimal('3.1')),
])
def test_operation_subtract(operand_a, operand_b, expected):
    assert Calculator.subtract(operand_a, operand_b) == expected

@pytest.mark.parametrize("operand_a, operand_b, expected", [
    (Decimal('3'), Decimal('4'), Decimal('12')),
    (Decimal('3.4'), Decimal('4.8'), Decimal('16.32')),
    (Decimal('0'), Decimal('4'), Decimal('0')),
    (Decimal('3'), Decimal('-4'), Decimal('-12')),
])
def test_operation_multiply(operand_a, operand_b, expected):
    assert Calculator.multiply(operand_a, operand_b) == expected
    assert Calculator.multiply(operand_b, operand_a) == expected

@pytest.mark.parametrize("operand_a, operand_b, expected", [
    (Decimal('12'), Decimal('4'), Decimal('3')),
    (Decimal('0'), Decimal('4'), Decimal('0')),
    (Decimal('3.8'), Decimal('2'), Decimal('1.9')),
])
def test_operation_division(operand_a, operand_b, expected):
    assert Calculator.division(operand_a, operand_b) == expected