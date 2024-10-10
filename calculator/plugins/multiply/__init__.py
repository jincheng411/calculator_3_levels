from aifc import Error
from decimal import Decimal
from calculator.calculator import Calculator
from calculator.commands import Command


class MultiplyCommand(Command):
    def execute(self, args: list):
        if len(args) != 2:
            print("Wrong number of arguments: multiply <num1> <num2>")
            return

        num1 = Decimal(args[0])
        num2 = Decimal(args[1])
        result = Calculator.multiply(num1, num2)
        print(f"{num1} * {num2} = {result}.")
