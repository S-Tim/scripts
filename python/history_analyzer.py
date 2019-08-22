#!/usr/bin/env python3

"""
Reads your terminal command history and groups commands to display their frequency.

Author: Tim Silhan
"""
import argparse
import subprocess
from pathlib import Path


def parse_arguments():
    parser = argparse.ArgumentParser(
        "Reads your terminal command history and groups commands to display their frequency.")
    parser.add_argument("shell_name", nargs="?", choices=[
                        "zsh", "bash"], default="zsh", help="The shell you are using")
    parser.add_argument("-n", "--number_of_commands", default=20,
                        help="Number of commands to print", type=int)
    return parser.parse_args()


def read_history(shell_name):
    hist_path = str(Path.home())

    if shell_name == "bash":
        hist_path += "/.bash_history"
    elif shell_name == "zsh":
        hist_path += "/.zsh_history"

    with open(hist_path, encoding="ISO-8859-1") as history:
        return format_history(shell_name, history.readlines())


def format_history(shell_name, history):

    if shell_name == "bash":
        formatted_history = history
    elif shell_name == "zsh":
        formatted_history = [entry.split(
            ";")[1] for entry in history if len(entry.split(";")) > 1]

    return [command.strip() for command in formatted_history]


def calculate_frequency(history):
    command_frequency = {}

    for command in history:
        if command in command_frequency.keys():
            command_frequency[command] += 1
        else:
            command_frequency[command] = 1

    return command_frequency


def sort_and_print_commands(command_frequency, number_of_items):
    sorted_command_frequency = sorted(
        command_frequency.items(), key=lambda entry: entry[1], reverse=True)

    if number_of_items <= 0 or number_of_items > len(command_frequency):
        print("Invalid number of items to display:", number_of_items)
        return

    for command, frequency in sorted_command_frequency[:number_of_items]:
        print(f"{command}: {frequency}")


if __name__ == "__main__":
    args = parse_arguments()
    history = read_history(args.shell_name)
    command_frequency = calculate_frequency(history)
    sort_and_print_commands(command_frequency, args.number_of_commands)
