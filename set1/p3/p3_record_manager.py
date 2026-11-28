"""
Name: Noel Jake Bernal
Section: IV-BSIT A
Activity: P3 - Student Record Manager
Date: November 27, 2026
"""


#set & lists

def add_student(students_list, unique_names_set):
    """
    Adds a student name to the records.
    Prevents duplicate entries (case-insensitive) using a set.
    """
    print("\n--- Add Student ---")
    name = input("Enter student name: ").strip()

    if not name:
        print("Error: Student name cannot be empty.")
        return

    # Check for duplicate entry (case-insensitive) using the set
    if name.lower() in unique_names_set:
        print(f"Duplicate Error: '{name}' already exists in the records. Entry rejected.")
        return

    # Store name in list and normalized lowercase in set
    students_list.append(name)
    unique_names_set.add(name.lower())
    print(f"Success: Student '{name}' successfully added!")

    t(f"Success: Student '{name}' successfully added!")


def remove_student(students_list, unique_names_set):
    """
    Removes a student name from the records (case-insensitive search).
    """
    print("\n--- Remove Student ---")
    if not students_list:
        print("Record is empty. No students to remove.")
        return

    name_to_remove = input("Enter student name to remove: ").strip()
    if not name_to_remove:
        print("Error: Input cannot be empty.")
        return

    # Find the exact name in list matching case-insensitively
    target_name = None
    for student in students_list:
        if student.lower() == name_to_remove.lower():
            target_name = student
            break

    if target_name:
        students_list.remove(target_name)
        unique_names_set.remove(target_name.lower())
        print(f"Success: Student '{target_name}' has been removed from records.")
    else:
        print(f"Not Found: No student found matching '{name_to_remove}'.")


def search_student(students_list):
    """
    Searches for students matching a partial name query.
    """
    print("\n--- Search Student ---")
    if not students_list:
        print("Record is empty. No students to search.")
        return

    query = input("Enter name or partial name to search: ").strip()
    if not query:
        print("Error: Search query cannot be empty.")
        return

    # Filter list for partial matches (case-insensitive)
    matches = [student for student in students_list if query.lower() in student.lower()]

    if matches:
        print(f"\nFound {len(matches)} matching student(s):")
        for idx, student in enumerate(matches, start=1):
            print(f"  {idx}. {student}")
    else:
        print(f"No students found matching '{query}'.")



def display_all_students(students_list):
    """
    Displays all students in alphabetical order, numbered, with total count.
    """
    print("\n--- All Students List ---")
    if not students_list:
        print("No student records available. The list is empty.")
        return

    # Sort students alphabetically without modifying original order
    sorted_students = sorted(students_list, key=str.lower)
    total_count = len(sorted_students)

    print(f"Total Students: {total_count}")
    print("-" * 35)
    for index, student in enumerate(sorted_students, start=1):
        print(f"{index}. {student}")
    print("-" * 35)


def show_menu():
    """
    Displays the user menu options.
    """
    print("\n" + "=" * 45)
    print("         STUDENT RECORD MANAGER")
    print("Student: Noel Jake Bernal | Section: IV-BSIT A")
    print("=" * 45)
    print("1. Add Student")
    print("2. Remove Student")
    print("3. Search Student (Partial Match)")
    print("4. Display All Students")
    print("5. Exit")
    print("=" * 45)

def main()

     # List: used to store ordered names for sorting and display
    students_list = []
    # Set: used for efficient, fast duplicate detection
    unique_names_set = set()