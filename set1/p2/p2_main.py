from datetime import datetime

import student_utils
from student_utils

import calculate_average, determine_pass_fail


def enter_grades():
    grades = []
    print("Enter the student's grades (0-100).")

    while True:
        try:
            grade = float(input("Enter a grade: "))
            if not 0 <= grade <= 100:
                print("Invalid input. Enter a number from 0 to 100.")
                continue
        except ValueError:
            print("Invalid input. Enter a number from 0 to 100.")
            continue

        grades.append(grade)
        choice = input("Enter another grade? (y/n): ").strip().lower()
        while choice not in ("y", "n"):
            print("Please enter y or n.")
            choice = input("Enter another grade? (y/n): ").strip().lower()
        if choice == "n":
            return grades


def main():
    grades = enter_grades()
    average = calculate_average(grades)
    status = determine_pass_fail(grades)
    highest = student_utils.get_highest_grade(grades)
    lowest = student_utils.get_lowest_grade(grades)

    print("\nStudent Grade Report")
    print(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Average: {average:.2f}")
    print(f"Highest: {highest:.2f}")
    print(f"Lowest: {lowest:.2f}")
    print(f"Status: {status}")


if __name__ == "__main__":
    main()
