def ana(word):
    letters = {}
    for i in set(word):
        letters[i] = word.count(i)
    return letters

def anagrams(word, words):
    res = []
    for x in words:
        if ana(x) == ana(word):
            res.append(x)
    return res
