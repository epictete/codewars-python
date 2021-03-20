def valid_parentheses(string):
    stack = []
    for i in string:
        if i == ")":
            if "(" in stack:
                stack.pop()
            else:
                return False
        elif i == "(":
            stack.append(i)
    return len(stack) == 0
