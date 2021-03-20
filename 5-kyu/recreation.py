# https://www.codewars.com/kata/55aa075506463dac6600010d/train/python

# Inspired by :
# https://stackoverflow.com/questions/53826181/optimization-of-codewars-python-3-6-code-integers-recreation-one

def list_squared(m, n):
    res = []
    for num in range(m, n):
        divi = set()
        for i in range(1, int(num**.5 + 1)):
            if num % i == 0:
                divi.add(int(num/i)**2)
                divi.add(i**2)
        total = sum(divi)**.5
        
        if total.is_integer():
            res.append([num, int(total)**2])
    return res

print(list_squared(42, 250))