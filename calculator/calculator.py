from decimal import Decimal
from typing import Callable

from calculator.calculation import Calculation
from calculator.history import History

class Calculator:
    @staticmethod
    def _perform_operation(a: Decimal, b: Decimal, operation: Callable[[Decimal, Decimal], Decimal]) -> Decimal:
        calculation = Calculation.create(a, b, operation)
        History.add_calculation(calculation)
        return calculation.perform()


