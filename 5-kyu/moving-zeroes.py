def move_zeros(array):
    stack = []
    zeros = []
    for i in array:
        if i == 0 and not i is False:
            zeros.append(i)
        else:
            stack.append(i)
    return stack + zeros
