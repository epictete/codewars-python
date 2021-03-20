def ana(word):
    letters = {}
    for i in set(word):
        letters[i] = word.count(i)
    return letters

def anagrams(word, words):
    return [i for i in words if ana(i) == ana(word)]
