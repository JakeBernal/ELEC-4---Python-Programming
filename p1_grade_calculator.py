
passingGrade = 75


def enterGrades():
    grades = []
    print("Enter your grades: ")

    while True:
        try:
            grade = float(input("Enter a grade (0-100): "))
            if grade < 0 or grade > 100:
                print("Invalid input. Please enter a grade between 0 and 100.")
                continue
            grades.append(grade)
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        choice = input("Do you want to enter another grade? (y/n): ")
        if choice.lower() != "y":
            break

    return grades
