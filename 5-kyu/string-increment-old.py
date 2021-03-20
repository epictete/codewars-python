def increment_string(strng):
    if strng == '':
        return '1'

    if strng.isalpha():
        return strng + '1'

    delimiter = -1

    for i in range(len(strng)):
        if strng[i].isdigit():
            delimiter = i
            break

    num = strng[delimiter:]

    return strng[:delimiter] + str(int(num)+1).zfill(len(num))



# print(increment_string("foo"), "foo1")
print(increment_string("foobar001"), "foobar002")
# print(increment_string("foobar1"), "foobar2")
# print(increment_string("foobar00"), "foobar01")
# print(increment_string("foobar99"), "foobar100")
# print(increment_string("foobar099"), "foobar100")
# print(increment_string(""), "1")