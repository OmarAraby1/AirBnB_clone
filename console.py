#!/usr/bin/python3
"""AirBnB Clone Command Line Interpreter

This script provides a basic command-line interface for interacting with
an Airbnb-like application.

Currently, it offers functionalities like displaying help and exiting.
More functionalities will be added as the project progresses.
"""
from cmd import Cmd


class AirBnBConsole(Cmd):
    """
    Class representing the Airbnb Console using the cmd module
    """

    prompt = "(hbnb) "
    intro = """
Welcome to the AirBnB Clone command-line interface!

Type 'help' for a list of available commands.
"""

    def do_help(self, arg):
        """
        Prints a list of available commands and their brief descriptions
        """
        if arg:
            print(f"No help available for '{arg}'.")
            return
        self.stdout.write(self.intro + "\n")
        self.stdout.write("Documented commands (type help <topic>):\n")
        super().do_help(arg)

    def do_quit(self, arg):
        """
        Exits the interpreter and closes the program
        """
        print("Exiting AirBnB Clone interpreter...")
        return True

    def emptyline(self):
        """
        Handles cases where user presses enter without input
        """
        pass

    def do_EOF(self, arg):
        """
        Exits the interpreter when user types Ctrl+D (EOF)
        """
        print()
        return True


if __name__ == "__main__":
    AirBnBConsole().cmdloop()
