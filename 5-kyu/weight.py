def red_max(num):
    x = sum([int(i) for i in num])
    return x if x < 10 else red(str(x))

def red(num):
    return sum([int(i) for i in num])

def order_weight(strng):
    arr = strng.strip().split()
    arr = sorted(arr, key=lambda x: (red(x), x))
    return arr

print(order_weight("103 123 4444 99 2000"))