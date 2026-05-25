def count_lines(file_path):
    try:
        with open(file_path, "r") as file:
            return sum(1 for _ in file)
        
    except FileNotFoundError:
        return -1    