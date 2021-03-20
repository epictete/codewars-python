def count_letters(s):

    s = [x for x in s if x.isalpha() and x.islower()]
    count_s = {}

    for letter in set(s):
        if s.count(letter) > 1:
            count_s[letter] = s.count(letter)
    
    return count_s

def mix(s1, s2):

    count_s1 = count_letters(s1)
    count_s2 = count_letters(s2)
    res = set()

    for key, val in count_s1.items():
        if val > count_s2.get(key, 0):
            res.add("1:" + val*key)
        elif val < count_s2.get(key, 0):
            res.add("2:" + count_s2.get(key, 0)*key)
        else:
            res.add("=:" + val*key)
    
    for key, val in count_s2.items():
        if val > count_s1.get(key, 0):
            res.add("2:" + val*key)
        elif val < count_s1.get(key, 0):
            res.add("1:" + count_s1.get(key, 0)*key)

    return "/".join(sorted(res, key=lambda x: (-len(x), x)))


# print(mix("Are they here", "yes, they are here"), "2:eeeee/2:yy/=:hh/=:rr")
print(mix("Sadus:cpms>orqn3zecwGvnznSgacs","MynwdKizfd$lvse+gnbaGydxyXzayp"), '2:yyyy/1:ccc/1:nnn/1:sss/2:ddd/=:aa/=:zz')
# print(mix("looping is fun but dangerous", "less dangerous than coding"), "1:ooo/1:uuu/2:sss/=:nnn/1:ii/2:aa/2:dd/2:ee/=:gg")
# print(mix(" In many languages", " there's a pair of functions"), "1:aaa/1:nnn/1:gg/2:ee/2:ff/2:ii/2:oo/2:rr/2:ss/2:tt")
# print(mix("Lords of the Fallen", "gamekult"), "1:ee/1:ll/1:oo")
# print(mix("codewars", "codewars"), "")
# print(mix("A generation must confront the looming ", "codewarrs"), "1:nnnnn/1:ooooo/1:tttt/1:eee/1:gg/1:ii/1:mm/=:rr")