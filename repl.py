import code
import sys

# definition of interactive console prompts
sys.ps1 = "hallpass >> "
sys.ps2 = "... "

# definition of custom Repl class
class Repl(code.InteractiveConsole):
    def runsource(self, source, filename="<input>", symbol="single"):
        if not source.endswith(";"):
            return True
        self.execute_cmd(source.strip(";"))
        return False

    # method to manually import the commands registry required for execute_cmd to access it
    def upload_registered_commands(self, registered_commands):
        self.registered_commands = registered_commands

    # method that performs command execution against what source content is provided in the REPL
    def execute_cmd(self, source:str):
        source_list = source.split()
        command = source_list[0]
        if len(source_list) == 1:
            args = list()
        else:
            args = source_list[1:]

        try:
            self.registered_commands.commands[command].cmd(args)
        except KeyError as e:
            print(f'The command {e} does not exist')
