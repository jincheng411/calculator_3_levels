import sys
from calculator.commands import Command


class ExitCommand(Command):
    def execute(self):
        print("Have a nice day!")
        sys.exit()