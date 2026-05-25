import os


def get_file_size(file_path):
    # Check if the path exists
    if not os.path.exists(file_path):
        return "File does not exist"

    # Check if the path is a file (not a directory)
    if not os.path.isfile(file_path):
        return "Path is not a file"

    # Return the file size in bytes
    return os.path.getsize(file_path)