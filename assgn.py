# File Creation
try:
    # Create a new text file named "my_file.txt" in write mode ('w')
    with open("my_file.txt", "w") as file:
        # Write at least three lines of text to the file
        file.write("This is line 1\n")
        file.write("12345\n")  # Writing a mix of string and number
        file.write("Another line of text\n")
        print("File created and initial data written successfully.")
except FileNotFoundError:
    print("Error: File not found or directory does not exist.")
except PermissionError:
    print("Error: Permission denied to create the file.")
finally:
    # File Reading and Display
    try:
        # Open "my_file.txt" in read mode ('r')
        with open("my_file.txt", "r") as file:
            # Read and display the contents of the file
            print("Contents of 'my_file.txt':")
            for line in file:
                print(line.strip())  # Remove newline characters for cleaner display
    except FileNotFoundError:
        print("Error: File not found or directory does not exist.")
    except PermissionError:
        print("Error: Permission denied to read the file.")
    finally:
        # File Appending
        try:
            # Open "my_file.txt" in append mode ('a')
            with open("my_file.txt", "a") as file:
                # Append three additional lines of text to the existing content
                file.write("Line 4 - Appended\n")
                file.write("54321\n")  # Appending a mix of string and number
                file.write("One more line appended\n")
                print("Additional data appended to 'my_file.txt'.")
        except FileNotFoundError:
            print("Error: File not found or directory does not exist.")
        except PermissionError:
            print("Error: Permission denied to append to the file.")