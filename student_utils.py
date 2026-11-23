PASSING_GRADE = 75


def calculate_average(grades):
    if not grades:
        return 0
    return sum(grades) / len(grades)


def determine_pass_fail(grades):
    if not grades:
        return "No grades entered"
    if calculate_average(grades) >= PASSING_GRADE:
        return "Passed"
    return "Failed"


def get_highest_grade(grades):
    if not grades:
        return None
    return max(grades)


def get_lowest_grade(grades):
    if not grades:
        return None
    return min(grades)
