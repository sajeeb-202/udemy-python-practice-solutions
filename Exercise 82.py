import os

def find_txt_files(directory):
    if not os.path.isdir(directory):
        return []

    txt_files = []

    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".txt"):
                txt_files.append(os.path.abspath(os.path.join(root, file)))

    return txt_files