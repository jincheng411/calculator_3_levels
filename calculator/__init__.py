from calculator.commands import CommandHandler
from calculator.commands.exit import ExitCommand


class App():
    def __init__(self):
        self.command_handler = CommandHandler()
    def start(self):
        self.command_handler.register_command("exit", ExitCommand())
        print("Welcome to the calculator, type 'exit' to stop.")
        while True:
            user_input = input(">>> ").strip()
            self.command_handler.execute_command(user_input)
            if user_input.lower() == "exit":
                print("Exiting...")
                break
            else:
                # Here, you could add additional commands and their handling
                print("Unknown command. Type 'exit' to exit.")