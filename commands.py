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

registered_commands = RegisteredCommands()

def register(*args):
    if len(args[0]) < 1:
        print("A user must be specified. Usage: register <username>")
    elif len(args[0]) > 1:
        print("The register command only accepts 1 user per call. Usage: register <username>")
    else:
        args_list = args[0]
        print(f'registering {args_list[0]}...')
            


def login(*args):
    print("log in a current user")

def help(*args):
    for cmd_str, cmd_obj in registered_commands.commands.items():
        print(f'{cmd_str}: {cmd_obj.description}')


Command("register", "registers new user", register, registered_commands)
Command("login", "logs in an existing user", login, registered_commands)
Command("help", "lists available commands", help, registered_commands)