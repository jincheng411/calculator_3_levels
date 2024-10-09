from decimal import Decimal
from calculator.calculator import Calculator
from calculator.commands import Command


class AddCommand(Command):
    def execute(self, args: list):
        if len(args) != 2:
            print("Wrong number of arguments: add <num1> <num2>")
            return

        try:
            num1 = Decimal(args[0])
            num2 = Decimal(args[1])
            result = Calculator.add(num1, num2)
            print(f"{num1} + {num2} = {result}.")
        except ValueError:
            print("Please enter valid numbers.")