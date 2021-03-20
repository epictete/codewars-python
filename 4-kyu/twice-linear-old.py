def dbl_linear(n):
    res = [1]
    i = 0
    while i < n :
        x = res[i]
        res.append(2*x + 1)
        res.append(3*x + 1)
        i += 1
        res.sort()
    return sorted(list(set(res)))[n]

print(dbl_linear(10), 22)
print(dbl_linear(20), 57)
print(dbl_linear(30), 91)
print(dbl_linear(50), 175)