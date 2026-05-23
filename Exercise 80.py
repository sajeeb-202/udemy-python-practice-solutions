def get_user_info():
    return ("Alice", 30, "alice@example.com")


def calculate_stats(numbers):
    if not numbers:
        return (0, 0, None, None)

    total = sum(numbers)
    average = total / len(numbers)
    minimum = min(numbers)
    maximum = max(numbers)

    return (total, average, minimum, maximum)


def split_name(full_name):
    if not full_name:
        return ("", "")

    parts = full_name.split()

    if len(parts) == 1:
        return (parts[0], "")

    return (parts[0], parts[-1])