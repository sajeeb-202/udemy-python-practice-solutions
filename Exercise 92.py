def compute_permutations(s):
    if len(s) <= 1:
        return [s]

    result = []

    for i in range(len(s)):
        char = s[i]
        remaining = s[:i] + s[i+1:]

        for perm in compute_permutations(remaining):
            result.append(char + perm)

    return result