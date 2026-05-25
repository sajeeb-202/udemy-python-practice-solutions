def capitalize_first_character(s):
    if not s or s.isspace():
        return s

    if not s[0].isalpha():
        return s

    first = s[0]

    # Handle German sharp s explicitly
    if first == "ß":
        return "ẞ" + s[1:]

    return first.upper() + s[1:]