opp = {
    "NORTH": "SOUTH",
    "SOUTH": "NORTH",
    "EAST": "WEST",
    "WEST": "EAST"
}

def dirReduc(arr):
    stack = []
    for i in arr:
        stack.append(i)
        if len(stack) > 1:
            if stack[-1] == opp[stack[-2]]:
                stack = stack[:-2]
    return stack
