def fib(num):
    stack = [0, 1]
    while True:
        a = stack[-2]
        b = stack[-1]
        next = a + b
        prod = a * b
        if prod < num:
            stack.append(next)
        else:
            return [a, b, prod == num]

print(fib(4895))