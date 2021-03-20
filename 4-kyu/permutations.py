import itertools

def permutations(string):
    return list(set("".join(list(i)) for i in itertools.permutations(string)))


print(sorted(permutations('a')), ['a'])
print(sorted(permutations('ab')), ['ab', 'ba'])
print(sorted(permutations('aabb')), ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa'])
# print(permutation("aabb"))