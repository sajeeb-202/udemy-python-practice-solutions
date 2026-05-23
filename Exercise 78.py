import os
def get_file_name(file_path):
    if not isinstance(file_path, str):
        return ""
        
    return os.path.basename(file_path)    