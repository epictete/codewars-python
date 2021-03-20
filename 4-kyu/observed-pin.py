def get_alts(num):

    keys = [
        [None, None, None, None, None],
        [None, "1", "2", "3", None],
        [None, "4", "5", "6", None],
        [None, "7", "8", "9", None],
        [None, None, "0", None, None],
        [None, None, None, None, None]
    ]

    index = []

    for line in keys:
        for key in line:
            if num == key:
                index += [keys.index(line), line.index(key)]
                break
    
    alts = []

    alts.append(num)
    alts.append(keys[index[0]-1][index[1]])
    alts.append(keys[index[0]+1][index[1]])
    alts.append(keys[index[0]][index[1]-1])
    alts.append(keys[index[0]][index[1]+1])

    return [x for x in alts if x is not None]

from itertools import product

def get_pins(observed):

    nums = [x for x in observed]
    alts = [get_alts(num) for num in nums]
    res = [list(x) for x in list(product(*alts))]

    return ["".join(x) for x in res]


print(get_pins('8'), ['5','7','8','9','0'])
print(get_pins('11'),["11", "22", "44", "12", "21", "14", "41", "24", "42"])
print(get_pins('369'), ["339","366","399","658","636","258","268","669","668","266","369","398","256","296","259","368","638","396","238","356","659","639","666","359","336","299","338","696","269","358","656","698","699","298","236","239"])
