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

def is_subject_validated(average):
    return average >= 10

def is_global_validated(report):
    for subject in report:
        if not subject["validation"]:
            return False
    return True

def print_grades(name, coefficient, grade, check_validation=False, indent=0):
    print("  " * indent, end="")
    print(f"{name}: {grade} ({coefficient}) ", end="")
    if check_validation:
        validation = is_subject_validated(grade)
        if validation: print("\033[92m" + "✔" + "\033[0m")
        else: print("\033[91m" + "✘" + "\033[0m")
    else: print()


def list_grades(data):
    report = []
    for subject in data["subjects"]:
        grade_subject = average(subject["exams"])
        report.append({
            "grade": grade_subject,
            "coefficient": subject["coefficient"],
            "validation": is_subject_validated(grade_subject)
        })
        print_grades(subject["name"], subject["coefficient"], grade_subject, check_validation=True)
        for exam in subject["exams"]:
            print_grades(exam["name"], exam["coefficient"], exam["grade"], indent=1)
    overall_grade = average(report)
    overall_validation = is_global_validated(report)
    is_compensation = False
    if not overall_validation and overall_grade >= 10:
        overall_validation = True
        is_compensation = True
    print(f"Overall grade: {overall_grade}", end="")
    if overall_validation:
        print(" \033[92m✔\033[0m", end="")
        if is_compensation:
            print(" (with compensation)")
        else: print()
    else: print(" \033[91m✘\033[0m")

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