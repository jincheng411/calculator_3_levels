from decimal import Decimal
from typing import Callable

from calculator import operations
from calculator.calculation import Calculation
from calculator.history import History

class Calculator:
    @staticmethod
    def _perform_operation(a: Decimal, b: Decimal, operation: Callable[[Decimal, Decimal], Decimal]) -> Decimal:
        calculation = Calculation.create(a, b, operation)
        History.add_calculation(calculation)
        return calculation.perform()

    @staticmethod
    def add(a: Decimal, b: Decimal) -> Decimal:
        return Calculator._perform_operation(a, b, operations.add)

    @staticmethod
    def subtract(a: Decimal, b: Decimal) -> Decimal:
        return Calculator._perform_operation(a, b, operations.subtract)

    @staticmethod
    def multiply(a: Decimal, b: Decimal) -> Decimal:
        return Calculator._perform_operation(a, b, operations.multiply)

    @staticmethod
    def division(a: Decimal, b: Decimal) -> Decimal:
        return Calculator._perform_operation(a, b, operations.division)


