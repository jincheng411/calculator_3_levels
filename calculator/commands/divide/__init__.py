from decimal import Decimal
from calculator.calculator import Calculator
from calculator.commands import Command


class DivideCommand(Command):
    def execute(self, operand_a, operand_b):
        print(f"{operand_a} / {operand_b} = {Calculator.division(Decimal(operand_a), Decimal(operand_b))}")