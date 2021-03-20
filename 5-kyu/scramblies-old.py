def scramble(s1, s2):
    ht = {}
    for char in s1:
        if char not in ht:
            ht[char] = 1
        else:
            ht[char] += 1
    for char in s2:
        if char in ht and ht[char] > 0:
            ht[char] -= 1
        else:
            return False
    return True
