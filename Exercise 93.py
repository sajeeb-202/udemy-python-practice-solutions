def countdown_timer(seconds):
    if seconds < 0:
        return "Invalid input: seconds must be non-negative."

    result = []

    for i in range(seconds, 0, -1):
        result.append(f"Time remaining: {i} seconds")

    result.append("Countdown complete!")
    return result