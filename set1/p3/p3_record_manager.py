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


def main()

     # List: used to store ordered names for sorting and display
    students_list = []
    # Set: used for efficient, fast duplicate detection
    unique_names_set = set()