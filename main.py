#!/bin/python

"""Entry executable"""

import sys
from help import help_needed, trigger_help
from file import find_data_filename, read_json_file
from grades import average_grade, is_period_validated

def calculate_grades(report):
    """
    Enrich the data with average grade and validation status of each subject.
    """
    for subject in report:
        subject["grade"] = average_grade(subject["exams"])
        subject["validated"] = subject["grade"] >= 10
    return report


def list_grades(data):
    """
    Print the content from the enriched data.
    """
    print(f"\033[1m{data['name']}\033[0m") # Title of the period in bold

    for subject in data["subjects"]:
        # Subject header line
        print(f"{subject['name']}: {subject['grade']} ({subject['coefficient']}) ", end="")
        if subject["validated"]:
            print("\033[92m" + "✔" + "\033[0m")
        else:
            print("\033[91m" + "✘" + "\033[0m")

        # Exams lines
        for exam in subject["exams"]:
            print(f"└ {exam['name']}: {exam['grade']} ({exam['coefficient']})")

    # Overall line
    period_validation_status = is_period_validated(data["subjects"])
    print(f"\033[1mOverall grade: {average_grade(data['subjects'])} ", end="")
    if period_validation_status == 0:
        print("\033[92m" + "✔" + "\033[0m")
    elif period_validation_status == 1:
        print("\033[92m" + "✔ (with compensation)" + "\033[0m")
    else:
        print("\033[91m" + "✘" + "\033[0m")

def print_error(message):
    """
    Print a red error message and exit the program.
    """
    print(f"\033[91mERROR: {message}\033[0m") # Print the error message in red
    sys.exit(0) # Exit the program

def run():
    """
    Entry function.
    """

    # If there is no argument or -h / --help passed in arguments
    if len(sys.argv) == 1 or help_needed():
        trigger_help() # Print help
        sys.exit(0) # Exit the program

    # Get the JSON filename from the arguments
    data_filename = find_data_filename()
    if data_filename is None:
        print_error("No JSON file passed as argument !")

    # Get the data from the JSON file
    data = read_json_file(data_filename)
    if data is None:
        print_error("JSON file passed as argument doesn't exist !")

    # Calculate the grades from the JSON data
    data["subjects"] = calculate_grades(data["subjects"])

    # List the grades from the JSON data
    list_grades(data)

if __name__ == "__main__":
    run()
