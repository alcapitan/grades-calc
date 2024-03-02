"""Module providing help feature."""

import sys

def help_needed():
    """
    Check if there is -h or --help in the command line arguments.
    """
    for param in sys.argv:
        if param == "-h" or param == "--help":
            return True
    return False

def trigger_help():
    """
    Print help content.
    """
    print("\033[1m", end="") # Make the text bold
    print("GRADES CALC")
    print("Author : @alcapitan on GitHub")
    # print("Version : unknown")
    print("License : GNU General Public License v3.0")
    print("Usage : python3 main.py <data.json>")
    print("\033[0m")
    print("A python script which sums school grades up, and calculates subject and overall grades.")
