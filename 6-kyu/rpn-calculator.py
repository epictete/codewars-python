operators = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a / b
}

def calc(expr):
    if not expr:
        return 0
    items = expr.split()
    stack = []
    for i in items:
        if i in operators:
            b = stack.pop()
            a = stack.pop()
            stack.append(operators[i](a, b))
        else:
            stack.append(float(i))

    return stack.pop()
