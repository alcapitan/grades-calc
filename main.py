import json

def read_json_file(file_path):
    with open(file_path, 'r') as file:
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


def run(filename):
    data = read_json_file(filename)
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
    run("model.json")