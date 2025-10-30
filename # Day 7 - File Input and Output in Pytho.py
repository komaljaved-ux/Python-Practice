# Day 7 - File Input and Output in Python 

# --- Writing to a File ---
# 'w' mode means write. It creates a new file or overwrites existing content.

def write_to_file(filename: str, content: str) -> None:
    """Write given content to a file."""
    with open(filename, "w") as file:
        file.write(content)
    print(f"Data written to {filename} successfully!")

# calling the function
write_to_file("day7_notes.txt", "Today I learned about file input and output in Python.\n")

# --- Reading from a File ---
# 'r' mode means read. It reads the file content.

def read_from_file(filename: str) -> None:
    """Read and display file content."""
    with open(filename, "r") as file:
        data: str = file.read()
    print("\nReading data from file:")
    print(data)

read_from_file("day7_notes.txt")

# --- Appending to a File ---
# 'a' mode means append. It adds data at the end of the file.

def append_to_file(filename: str, new_content: str) -> None:
    """Append new content to an existing file."""
    with open(filename, "a") as file:
        file.write(new_content)
    print(f"New data appended to {filename} successfully!")

append_to_file("day7_notes.txt", "I also learned how to append new data to a file.\n")

# Reading again after append
read_from_file("day7_notes.txt")

# --- Writing Multiple Lines ---
def write_list_to_file(filename: str, lines: list[str]) -> None:
    """Write multiple lines to a file."""
    with open(filename, "w") as file:
        for line in lines:
            file.write(line + "\n")
    print(f"List of lines written to {filename} successfully!")

my_notes: list[str] = [
    "File handling is used to store data permanently.",
    "We can use 'w', 'r', and 'a' modes.",
    "Always close the file or use 'with open'."
]

write_list_to_file("file_tips.txt", my_notes)
read_from_file("file_tips.txt")