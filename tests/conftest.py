'''conftest.py'''
import pytest
from decimal import Decimal
from faker import Faker
from calculator.operations import add, subtract, multiply, division

fake = Faker()

def generate_test_data(num_records):
    operation_mappings = {
        'add': add,
        'subtract': subtract,
        'multiply': multiply,
        'divide': division
    }
    for _ in range(num_records):
        operand_a = Decimal(fake.random_number(digits=2))
        operand_b = Decimal(fake.random_number(digits=2)) if _ % 4 != 3 else Decimal(fake.random_number(digits=1))
        operation = fake.random_element(elements=list(operation_mappings.keys()))
        operation_func = operation_mappings[operation]

        if operation_func == division:
            operand_b = Decimal('1') if operand_b == Decimal('0') else operand_b

        try:
            if operation_func == division and operand_b == Decimal('0'):
                expected = "ZeroDivisionError"
            else:
                expected = operation_func(operand_a, operand_b)
        except ZeroDivisionError:
            expected = "ZeroDivisionError"

        yield operand_a, operand_b, operation, operation_func, expected

def pytest_addoption(parser):
    parser.addoption("--num_records", action="store", default=5, type=int, help="Number of test records to generate")

def pytest_generate_tests(metafunc):
    ''' Check if the test is expecting any of the dynamically generated fixtures'''
    if {"operand_a", "operand_b", "expected"}.intersection(set(metafunc.fixturenames)):
        num_records = metafunc.config.getoption("num_records")
        # Adjust the parameterization to include both operation and operation for broad compatibility
        # Ensure 'operation' is used for identifying the operation in Calculator class tests
        # 'operation' (function reference) is used for Calculation class tests.
        parameters = list(generate_test_data(num_records))
        # Modify parameters to fit test functions' expectations
        print(metafunc.fixturenames)
        modified_parameters = [(a, b, op_name if 'operation_name' in metafunc.fixturenames else op_func, expected) for a, b, op_name, op_func, expected in parameters]
        metafunc.parametrize("operand_a,operand_b,operation,expected", modified_parameters)
