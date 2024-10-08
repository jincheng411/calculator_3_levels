from abc import ABC, abstractmethod


class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

class CommandHandler:
    def __init__(self):
        self.commands = {}

    def register_command(self, command_name: str, command: Command):
        self.commands[command_name] = command

    def execute_command(self, command_name: str):
        command_arr = command_name.split(' ')
        if command_arr[0] in self.commands:
            if len(command_arr) == 1 and command_arr[0].lower() == 'exit':
                self.commands[command_arr[0]].execute()
            else:
                if len(command_arr) == 3:
                    self.commands[command_arr[0]].execute(command_arr[1], command_arr[2])
                else:
                    print(f"Wrong number of arguments for command '{command_arr[0]}'")
        else:
            print(f"No such command: {command_name}")