def factors(n):
    n = abs(n)
    lst = []
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            while n % i == 0:
                n = n / i
            lst.append(i)
    if n != 1:
        lst.append(int(n))
    return lst


def sum_for_list(lst):
    prime_fact = []
    res = {}
    for i in lst:
        res.setdefault(i, [])
        res[i] += factors(i)
        prime_fact += factors(i)
    print(prime_fact)
    print(res)
    final = []
    for i in set(prime_fact):
        sum_fact = 0
        tmp = [i]
        for k, v in res.items():
            if i in v:
                sum_fact += int(k) * v.count(i)
        tmp.append(sum_fact)
        final.append(tmp)
    return sorted(final)


print(sum_for_list([-12, -12]))
