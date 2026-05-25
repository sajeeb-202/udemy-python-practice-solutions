def reverse_number(n):
    # Handle negative numbers
    if n < 0:
        digits = list(str(abs(n)))   # Convert positive part to list
        digits.reverse()             # Reverse the list
        return -int("".join(digits)) # Join and restore negative sign

    # Handle positive numbers and zero
    digits = list(str(n))            # Convert number to list of digits
    digits.reverse()                 # Reverse the list
    return int("".join(digits))      # Convert back to integer