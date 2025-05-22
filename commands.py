from termcolor import colored
from login import register_user

# definitions for commands registry and command classes
class RegisteredCommands():
    def __init__(self):
        self.commands = dict()

class Command():
    def __init__(self, name:str, description:str, command, reg_cmd_obj):
        self.name = name
        self.description = description
        # consider adding usage example to be displayed with "help" command
        self.cmd = command
        self.register_command(reg_cmd_obj)

    def register_command(self, reg_cmd_obj):
        reg_cmd_obj.commands[self.name] = self

# instantiate commands registry
registered_commands = RegisteredCommands() # available to main as export

# collection of available commands
def register(*args):
    if len(args[0]) < 1:
        print("A user must be specified. Usage: register <username>")
    elif len(args[0]) > 1:
        print("The register command only accepts 1 user per call. Usage: register <username>")
    else:
        args_list = args[0]
        username = args_list[0]
        try:
            register_user(username)
            print(colored("User successfully created!", "green"))
        except Exception as e:
            print(f'Error: {e}')
            
def login(*args):
    print("log in a current user")

def help(*args):
    for cmd_str, cmd_obj in registered_commands.commands.items():
        print(f'{cmd_str}: {cmd_obj.description}')

# instantiate commands
Command("register", "registers new user", register, registered_commands)
Command("login", "logs in an existing user", login, registered_commands)
Command("help", "lists available commands", help, registered_commands)