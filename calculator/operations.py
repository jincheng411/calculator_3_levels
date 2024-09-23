from decimal import Decimal


class Operations:
    @staticmethod
    def add(a: Decimal, b: Decimal) -> Decimal:
        return a + b

    @staticmethod
    def substract(a: Decimal, b: Decimal) -> Decimal:
        return a - b

    @staticmethod
    def multiply(a: Decimal, b: Decimal) -> Decimal:
        return a * b

    @staticmethod
    def division(a: Decimal, b: Decimal) -> Decimal:
        return a / b
