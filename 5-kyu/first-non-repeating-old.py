def first_non_repeating_letter(string):
    if len(string) < 2:
        return string
    if len(set(string)) == len(string) / 2:
        return ""
    seen = []
    for i in range(len(string)):
        if string[i].lower() not in seen:
            seen.append(string[i].lower())
        else:
            continue
        count = 0
        for j in range(i, len(string)):
            if string[i].lower() == string[j].lower():
                count += 1
        if count == 1:
            return string[i]
