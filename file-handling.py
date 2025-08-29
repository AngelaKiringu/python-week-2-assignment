try:
    filename = input("Enter the filename to read: ")
    with open(filename, 'r') as file:
        content = file.read()

    # Modify content (example: convert to uppercase)
    modified_content = content.upper()

    # Write modified content to a new file
    with open('modified_' + filename, 'w') as new_file:
        new_file.write(modified_content)

    print(f"Modified content written to 'modified_{filename}'")

except FileNotFoundError:
    print("Error: The file does not exist.")
except IOError:
    print("Error: Could not read/write the file.")
