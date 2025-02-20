import os  # Import os to check file existence

def write_file(file_name, file_content):
    """Writes file_content to a .txt file, overwriting existing content if any."""
    with open(f"{file_name}.txt", "w", encoding="utf-8") as file:
        file.write(file_content)

def append_file(file_name, append_content):
    """Appends append_content to an existing .txt file without extra blank lines."""
    file_path = f"{file_name}.txt"

    with open(file_path, "a", encoding="utf-8") as file:
        # Only add a newline if the file is not empty and append_content doesn't already start with '\n'
        if os.path.getsize(file_path) > 0 and not append_content.startswith("\n"):
            file.write("\n")
        file.write(append_content)

def read_file(file_name):
    """Reads and returns the content of a .txt file."""
    file_path = f"{file_name}.txt"

    if not os.path.exists(file_path):
        return ""  # Return an empty string if the file does not exist

    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


