#!/usr/bin/python3
"""AirBnB Clone Command Line Interpreter

This script provides a basic command-line interface for interacting with
an Airbnb-like application.

Currently, it offers functionalities like displaying help and exiting.
More functionalities will be added as the project progresses.
"""

def main():
    """Main function for the command-line interpreter

    This function runs the interpreter in an interactive loop,
    allowing users to enter commands and receive responses.
    """

    commands = {"help": print_help, "quit": exit_interpreter}

    while True:
        prompt = "(hbnb) "
        user_input = input(prompt)

        if not user_input:
            continue

        if user_input.lower() in commands:
            commands[user_input.lower()]()
        else:
            print(f"Invalid command: '{user_input}'. Use 'help' for a list.")


def print_help():
    """Prints a list of available commands and their brief descriptions"""

    print("""
Documented commands (type help <topic>):
  ========================================
  EOF   help  quit
""")


def exit_interpreter():
    """Exits the interpreter and closes the program"""

    print("Exiting AirBnB Clone interpreter...")
    exit(0)


if __name__ == "__main__":
    main()
