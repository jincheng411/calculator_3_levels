from decimal import Decimal



def add(a: Decimal, b: Decimal) -> Decimal:
    return a + b


def subtract(a: Decimal, b: Decimal) -> Decimal:
    return a - b


def multiply(a: Decimal, b: Decimal) -> Decimal:
    return a * b


def division(a: Decimal, b: Decimal) -> Decimal:
    # if b == 0:
    #     raise ZeroDivisionError
    # return a / b
    try:
        return a / b
    except ZeroDivisionError:
        print("can not divide by zero")
