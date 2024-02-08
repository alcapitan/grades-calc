#!/bin/python

import sys, os, json

def find_data_file():
    for param in sys.argv:
        if param.endswith(".json"):
            return param

def read_json_file(filename):
    if not os.path.isfile(filename):
        return None
    with open(filename, 'r') as file:
        return json.load(file)

def average(list):
    sum = coef = result = 0
    for exam in list:
        coef += exam["coefficient"]
        sum += exam["grade"] * exam["coefficient"]

    if coef != 0:
        result = sum / coef
        result = round(result, 2)
    return result

def print_grades(name, coefficient, grade, indent=0):
    print("  " * indent, end="")
    print(f"{name}: {grade} ({coefficient})")


def list_grades(data):
    report = []
    for subject in data["subjects"]:
        grade_subject = average(subject["exams"])
        report.append({
            "grade": grade_subject,
            "coefficient": subject["coefficient"]
        })
        print_grades(subject["name"], subject["coefficient"], grade_subject)
        for exam in subject["exams"]:
            print_grades(exam["name"], exam["coefficient"], exam["grade"], indent=1)
    print(f"Overall grade: {average(report)}")

if __name__ == "__main__":
    data_file = find_data_file()
    if data_file is None:
        print("ERROR: No JSON file passed as argument")
    else:
        data = read_json_file(data_file)
        if data is None:
            print("ERROR: JSON file doesn't exist")
        else:
            list_grades(data)