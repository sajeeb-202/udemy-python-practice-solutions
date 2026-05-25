import os
import platform
from datetime import datetime


def get_file_dates(file_path):
    # Check if the file exists
    if not os.path.exists(file_path):
        return "File not found"

    # Get file metadata (timestamps and other info)
    file_stats = os.stat(file_path)

    # Convert modification timestamp to readable format
    modification_date = datetime.fromtimestamp(
        file_stats.st_mtime
    ).strftime("%Y-%m-%d %H:%M:%S")

    # Handle creation date based on operating system
    if platform.system() == "Windows":
        # Windows provides creation time in st_ctime
        creation_date = datetime.fromtimestamp(
            file_stats.st_ctime
        ).strftime("%Y-%m-%d %H:%M:%S")

    elif platform.system() == "Darwin":
        # macOS provides creation time in st_birthtime
        creation_date = datetime.fromtimestamp(
            file_stats.st_birthtime
        ).strftime("%Y-%m-%d %H:%M:%S")

    else:
        # Linux usually does not provide file creation time
        creation_date = "Creation date not available"

    # Return results as a dictionary
    return {
        "creation_date": creation_date,
        "modification_date": modification_date
    }