import sys
#from login import register_user
from repl import Repl
from commands import registered_commands

def main():
    # Instantiate the REPL
    repl = Repl()
    repl.upload_registered_commands(registered_commands)
    repl.interact(banner="Welcome to HallPass! Commands must end with ';'", exitmsg="Quitting HallPass...")

main()
