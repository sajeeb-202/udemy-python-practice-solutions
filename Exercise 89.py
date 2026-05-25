def count_digits(number):
    # Convert negative number to positive, then convert to string and count characters
    return len(str(abs(number)))