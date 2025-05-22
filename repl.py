import code
import sys

""" class HPRepl(code.InteractiveConsole):
    def runsource(self, source, filename="<input>", symbol="single"):
        print("source:", source)
        return True
    
repl = HPRepl(locals={'my_var': 'Hello, World!'})
repl.interact(banner="Welcome to HPRepl", exitmsg="Goodbye!") """

sys.ps1 = "hallpass >> "
sys.ps2 = "... "


class Repl(code.InteractiveConsole):
    def runsource(self, source, filename="<input>", symbol="single"):
        if not source.endswith(";"):
            return True
        self.execute_cmd(source.strip(";"))
        return False

    def upload_registered_commands(self, registered_commands):
        self.registered_commands = registered_commands

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
