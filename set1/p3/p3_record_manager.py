"""
Name: Noel Jake Bernal
Section: IV-BSIT A
Activity: P3 - Student Record Manager
Date: November 27, 2026
"""


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
