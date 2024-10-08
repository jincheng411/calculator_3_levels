import sys
from calculator import App
from calculator.calculator import Calculator
from decimal import Decimal, InvalidOperation
from calculator.operations import add, subtract, multiply, division


# def calculate_and_print(operand_a, operand_b, operation):
#     operation_mappings = {
#         'add': add,
#         'subtract': subtract,
#         'multiply': multiply,
#         'divide': division
#     }

#     try:
#         decimal_a = Decimal(operand_a)
#         decimal_b = Decimal(operand_b)
#         result = operation_mappings.get(operation)
#         if result:
#             print(f"The result of {operand_a} {operation} {operand_b} is equal to {result(decimal_a, decimal_b)}")
#         else:
#             print(f"Unknown operation: {operation}")
#     except InvalidOperation:
#         print(f"Invalid number input: {operand_a} or {operand_b} is not a valid number.")
#     except ZeroDivisionError:
#         print("Error: Division by zero.")
#     except Exception as e:
#         print(f"An error occurred: {e}")

# def main():
#     if len(sys.argv) != 4:
#         print("Usage: python calculator_main.py <number1> <number2> <operation>")
#         sys.exit(1)

#     _, a, b, operation = sys.argv
#     calculate_and_print(a, b, operation)

if __name__ == '__main__':
    app = App()
    app.start()
