"""
File Handling Basics
====================
File handling in Python involves opening, reading, writing, and closing files. The `open()` function 
is used to access files, and using the `with` statement ensures files are properly closed after operations.

Core Concepts:
- Modes:
  - `r`: Read (default mode).
  - `w`: Write (overwrites the file).
  - `a`: Append (adds to the file without overwriting).
  - `rb`, `wb`: Read/write in binary mode.
- The `with` Statement:
  Ensures proper file closure, even if an exception occurs during file operations.
"""

def read_file(filepath):
    """
    Reads and prints the content of a file.

    Args:
        filepath (str): Path to the file.
    
    Returns:
        str: Content of the file.
    """
    try:
        with open(filepath, 'r') as file:  # Open in read mode
            content = file.read()  # Read entire content
            return content
    except FileNotFoundError:
        return "File not found. Please provide a valid file path."

def write_file(filepath, content):
    """
    Writes content to a file (overwrites existing content).

    Args:
        filepath (str): Path to the file.
        content (str): Content to write.
    """
    with open(filepath, 'w') as file:  # Open in write mode
        file.write(content)
    return "Content written successfully."

def append_to_file(filepath, content):
    """
    Appends content to an existing file.

    Args:
        filepath (str): Path to the file.
        content (str): Content to append.
    """
    with open(filepath, 'a') as file:  # Open in append mode
        file.write(content + '\n')
    return "Content appended successfully."

# Testing the functions
if __name__ == "__main__":
    test_file = "example.txt"

    # Writing content to a file
    print(write_file(test_file, "This is a new file."))
    
    # Reading content from the file
    print("File Content:", read_file(test_file))
    
    # Appending content to the file
    print(append_to_file(test_file, "This is an appended line."))
    
    # Reading the updated file
    print("Updated File Content:", read_file(test_file))
