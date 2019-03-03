#!/usr/bin/env python3

"""
This script runs all the bash commands passed as arugments. Alternatively the
run_command function can be imported from another script.

Example:
    run-commands.py "ls -l" "echo Hello World!"

Author: Tim Silhan
"""
from subprocess import call

def run_command(command):
    call(command.split(" "))

if __name__ == "__main__":
    import sys

    for arg in sys.argv[1:]:
        run_command(arg)

