from calculator.commands import Command


class ExitCommand(Command):
    def execute(self):
        print("Bye.")