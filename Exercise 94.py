def count_character_occurrences(string, char):
    if len(char) != 1:
        return "Input character must be a single character."
    return string.count(char)