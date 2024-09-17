# file_handling_assignment.py

def create_and_write_file(filename):
    try:
        # Open the file in write mode
        with open(filename, 'w') as file:
            # Write initial lines to the file
            file.write("This is the first line.\n")
            file.write("Here is the second line with a number: 42\n")
            file.write("Finally, the third line with a mix of numbers and letters: abc123\n")
        print("Initial content written successfully.")
    except (FileNotFoundError, PermissionError) as e:
        print(f"Error writing to file: {e}")
    finally:
        print("File writing operation completed.")

def read_and_display_file(filename):
    try:
        # Open the file in read mode
        with open(filename, 'r') as file:
            # Read and display the contents of the file
            content = file.read()
            print("\nFile Content:")
            print(content)
    except (FileNotFoundError, PermissionError) as e:
        print(f"Error reading file: {e}")
    finally:
        print("File reading operation completed.")

def append_to_file(filename):
    try:
        # Open the file in append mode
        with open(filename, 'a') as file:
            # Append additional lines to the file
            file.write("Appending the fourth line.\n")
            file.write("Appending the fifth line with a number: 12345\n")
            file.write("Appending the sixth line with some more text.\n")
        print("Additional content appended successfully.")
    except (FileNotFoundError, PermissionError) as e:
        print(f"Error appending to file: {e}")
    finally:
        print("File appending operation completed.")

if __name__ == "__main__":
    filename = "my_file.txt"
    create_and_write_file(filename)
    read_and_display_file(filename)
    append_to_file(filename)
    read_and_display_file(filename)
