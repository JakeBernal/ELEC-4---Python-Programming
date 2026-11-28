"""
Name: Noel Jake Bernal
Section: IV-BSIT A
Activity: P4 - Safe Menu Program (Exception Handling)
Date: November 28, 2026
"""

def perform_division():
    """
    Demonstrates handling ValueError and ZeroDivisionError.
    Uses try, except, else, and finally blocks.
    """
    print("\n--- Division Operation ---")
    try:
        num1_str = input("Enter numerator (first number): ").strip()
        num1 = float(num1_str)

        num2_str = input("Enter denominator (second number): ").strip()
        num2 = float(num2_str)

        result = num1 / num2

    except ValueError:
        # Handles non-numeric input
        print("Error [ValueError]: Invalid input. You must enter valid numerical values.")
    except ZeroDivisionError:
        # Handles attempt to divide by zero
        print("Error [ZeroDivisionError]: Division by zero is not allowed.")
    else:
        # Executes only when no exception occurs
        print(f"Success: {num1} / {num2} = {result:.4f}")
    finally:
        # Executes regardless of outcome
        print("[Status] Division attempt finished.\n")


def open_and_read_file():
    """
    Demonstrates handling FileNotFoundError when reading a file.
    Uses try, except, else, and finally blocks.
    """
    print("\n--- Open and Read File ---")
    filename = input("Enter the file name or relative path: ").strip()

    file_obj = None
    try:
        # Attempt to open the specified file for reading
        file_obj = open(filename, "r", encoding="utf-8")
        content = file_obj.read()
    except FileNotFoundError:
        # Handles missing file error
        print(f"Error [FileNotFoundError]: The file '{filename}' was not found.")
    else:
        # Executes only when file was opened and read successfully
        print("\n--- File Content ---")
        print(content)
        print("--------------------")
    finally:
        # Ensure file handle is closed if it was opened
        if file_obj:
            file_obj.close()
            print(f"[Status] File '{filename}' was safely closed.")
        else:
            print("[Status] File operation terminated.\n")


def show_menu():
    """
    Displays the menu options.
    """
    print("\n" + "=" * 45)
    print("         SAFE MENU PROGRAM")
    print("Student: Noel Jake Bernal | Section: IV-BSIT A")
    print("=" * 45)
    print("1. Perform Division")
    print("2. Open and Read a File")
    print("3. Exit")
    print("=" * 45)


def main():
    """
    Main loop ensuring the program never crashes on invalid inputs.
    """
    while True:
        show_menu()
        choice = input("Select an option (1-3): ").strip()

        if choice == "1":
            perform_division()
        elif choice == "2":
            open_and_read_file()
        elif choice == "3":
            print("\nExiting Safe Menu Program. Goodbye!")
            break
        else:
            # Handles invalid menu choices safely without crashing
            print(f"Error: '{choice}' is not a valid menu choice. Please select 1, 2, or 3.")


if __name__ == "__main__":
    main()
