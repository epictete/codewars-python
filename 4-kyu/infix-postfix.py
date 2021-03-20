def get_weight(op):
    if op in ['+', '-']:
        return 1
    if op in ['*', '/']:
        return 2
    if op == '^':
        return 3


def has_precedence(op1, op2):
    op1 = get_weight(op1)
    op2 = get_weight(op2)
    if op1 == op2:
        return op1 != 3
    return op1 > op2


def to_postfix (infix):
    stack = []
    res = ""
    for char in infix:
        if char.isdigit():
            res += char
        if char in ['+', '-', '*', '/', '^']:
            while len(stack) > 0 and stack[-1] != '(' and has_precedence(stack[-1], char):
                res += stack.pop()
            stack.append(char)
        if char == '(':
            stack.append(char)
        if char == ')':
            while len(stack) > 0 and stack[-1] != '(':
                res += stack.pop()
            stack.pop()
    while len(stack) > 0:
        res += stack.pop()
    return res


# print(to_postfix("2+7*5"), "275*+")
# print(to_postfix("3*3/(7+1)"), "33*71+/")
# print(to_postfix("5+(6-2)*9+3^(7-1)"), "562-9*+371-^+")
# print(to_postfix("(5-4-1)+9/5/2-7/1/7"), "54-1-95/2/+71/7/-")
print(to_postfix("1^2^3"), "123^^")
