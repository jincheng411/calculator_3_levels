from calculator.commands import Command


class AddCommand(Command):
    def execute(self, operand_a, operand_b):
        print(f"{operand_a} + {operand_b} = {operand_a + operand_b}")