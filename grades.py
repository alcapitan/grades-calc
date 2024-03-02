"""Module for manipulating grades"""

def average_grade(report):
    """
    Return the average grade of a list of exams taking coefficients into account.
    """
    total = coef = result = 0
    for exam in report:
        coef += exam["coefficient"]
        total += exam["grade"] * exam["coefficient"]

    if coef != 0:
        result = total / coef
        result = round(result, 2)

    return result

def is_period_validated(report):
    """
    Return if the period is validated or not.
    This is accorded to my university's rules.
    Return 0 if the period is validated, this means every subject has been validated.
    Return 1 if the period is validated with compensation, this means the overall grade is >= 10. 
    Return 2 if the period is not validated, this means you do not check the previous conditions.
    """
    # Check if every subject has been validated
    if all(subject["validated"] for subject in report):
        return 0
    # Check if the overall grade is >= 10
    elif average_grade(report) >= 10:
        return 1
    # If neither condition is met
    else:
        return 2
