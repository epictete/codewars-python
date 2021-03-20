def next_bigger(n):
    num = list(str(n))

    if int("".join(sorted(num, reverse=True))) == n:
        return -1
    
    for i in range(1, len(num) + 1):
        x = num[-i:]
        if x[0] < max(x):
            tmp = sorted([j for j in x if j > x[0]])[0]
            x.remove(tmp)
            a = "".join(num[:-i])
            b = [tmp + "".join(sorted(x))]
            return int(a + b[0])


    



print(next_bigger(12),21)
print(next_bigger(513),531)
print(next_bigger(2017),2071)
print(next_bigger(2071),2107)
print(next_bigger(414),441)
print(next_bigger(144),414)
