from decimal import Decimal

class Operations:
    @staticmethod
    def add(a: Decimal, b: Decimal) -> Decimal:
        return a + b

    @staticmethod
    def subtract(a: Decimal, b: Decimal) -> Decimal:
        return a - b

    @staticmethod
    def multiply(a:
        Decimal, b: Decimal) -> Decimal:
        return a * b

    @staticmethod
    def division(a: Decimal, b: Decimal) -> Decimal:
        if b == 0:
            raise ZeroDivisionError
        return a / b
