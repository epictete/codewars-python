# https://www.codewars.com/kata/55aa075506463dac6600010d/train/python

def div(n):
    divisors = set()
    for i in range(1, n + 1):
        if n % i == 0:
            divisors.add(int(n/i)**2)
            divisors.add(i**2)
    return sum(divisors)

def list_squared(m, n):
    print(f"m: {m}, n: {n}", flush=True)
    res = []
    for i in range(m, n):
        if (div(i)**.5).is_integer():
            res.append([i, div(i)])
    return res

print(list_squared(1, 250))