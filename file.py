"""Module for managing data files."""

import sys
import os
import json

def find_data_filename():
    """
    Return the name of the json data file passed in the command.
    Return None if no json file was set in the command.
    """
    for param in sys.argv:
        if param.endswith(".json"):
            return param
    return None

def read_json_file(filename):
    """
    Read a json file and return its content.
    Return None if the file doesn't exist.
    """
    if not os.path.isfile(filename):
        return None
    with open(filename, 'r', encoding="utf-8") as file:
        return json.load(file)
