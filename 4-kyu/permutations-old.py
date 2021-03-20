import itertools

def permutations(string):
    res = set()
    for i in itertools.permutations(string):
        res.add("".join(list(i)))
    return list(res)
