def are_anagrams(str1, str2):
    # Remove special characters/spaces and convert to lowercase
    clean1 = ''.join(sorted(char.lower() for char in str1 if char.isalnum()))
    clean2 = ''.join(sorted(char.lower() for char in str2 if char.isalnum()))

    # Compare cleaned strings
    return clean1 == clean2