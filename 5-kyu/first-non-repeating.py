def first_non_repeating_letter(string):
    lower = string.lower()
    for i, char in enumerate(lower):
        if lower.count(char) == 1:
            return string[i]
    return ""
