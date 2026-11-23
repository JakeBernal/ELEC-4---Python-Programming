passingGrade = 75


def enterGrades():
    grades = []
    print("\nEnter the student's grades.")

    while True:
        try:
            grade = float(input("Enter a grade (0-100): "))
            if not 0 <= grade <= 100:
                print("Invalid input. Please enter a grade between 0 and 100.")
                continue
            elif grade <= 70:
                print("You can't input grades lower than 70 ")


        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        grades.append(grade)
        choice = input("Do you want to enter another grade? (y/n): ").lower()
        while choice not in ("y", "n"):
            print("Please enter y or n.")
            choice = input("Do you want to enter another grade? (y/n): ").lower()
        if choice == "n":
            break

    return grades


def calculateAverage(grades):
    if not grades:
        return 0
    return sum(grades) / len(grades)


def getHighestGrade(grades):
    if not grades:
        return None
    return max(grades)


def getLowestGrade(grades):
    if not grades:
        return None
    return min(grades)


def getPassFailStatus(grades):
    if not grades:
        return "No grades entered"
    if calculateAverage(grades) >= passingGrade:
        return "Passed"
    return "Failed"


def displayResults(grades):
    average = calculateAverage(grades)
    highest = getHighestGrade(grades)
    lowest = getLowestGrade(grades)
    status = getPassFailStatus(grades)

    print("\nStudent Grade Results")
    print(f"Average: {average:.2f}")
    print(f"Highest: {highest:.2f}")
    print(f"Lowest: {lowest:.2f}")
    print(f"Status: {status}")


def main():
    grades = []

    while True:
        print("\nStudent Grade Calculator")
        print("1. Enter grades")
        print("2. View results")
        print("3. Exit")
        choice = input("Choose an option (1-3): ").strip()

        if choice == "1":
            grades.extend(enterGrades())
        elif choice == "2":
            if grades:
                displayResults(grades)
            else:
                print("No grades entered yet. Choose option 1 first.")
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose 1, 2, or 3.")


if __name__ == "__main__":
    main()

# The global variable passingGrade is defined outside all functions and can be used
# throughout this program. The grades variable inside enterGrades is local to that
# function, so it only exists there unless the function returns it. In main, grades
# is a different local variable that stores the grades returned by enterGrades.
