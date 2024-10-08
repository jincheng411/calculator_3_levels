from calculator.commands import CommandHandler
from calculator.commands.add import AddCommand
from calculator.commands.exit import ExitCommand


class App():
    def __init__(self):
        self.command_handler = CommandHandler()
    def start(self):
        self.command_handler.register_command("exit", ExitCommand())
        self.command_handler.register_command("add", AddCommand())
        print("Welcome to the calculator, type 'exit' to stop.")
        while True:
            user_input = input(">>> ").strip()
            # input_arr = user_input.split(' ')
            self.command_handler.execute_command(user_input)
            # if input_arr[0].lower() == "exit":
            #     print("Exiting...")
            #     break
            # else:
            #     # Here, you could add additional commands and their handling
            #     print("Unknown command. Type 'exit' to exit.")