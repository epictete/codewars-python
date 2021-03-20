def solution(args):
    res = []
    stack = []
    
    for i in range(len(args) - 1):
        if args[i+1] - args[i] == 1:
            stack.append(args[i])
            stack.append(args[i+1])
            if i+1 == len(args) - 1:
                res.append(sorted(list(set(stack))))
        else:
            if len(stack) > 0:
                res.append(sorted(list(set(stack))))
                stack = []
            else:
                res.append(args[i])
    
    if args[-1] - args[-2] > 1:
        res.append(args[-1])

    x = ""

    for j in res:
        if isinstance(j, int):
            x += str(j) + ","
        elif len(j) == 2:
            x += str(j[0]) + "," + str(j[1]) + ","
        else:
            x += str(j[0]) + "-" + str(j[-1]) + ","
    
    return x.strip(',')



print(solution([-59, -56, -53, -51, -48, -47, -45, -44, -41, -39, -37, -34, -33, -31, -28, -26, -23, -20, -19, -17, -15, -12, -10, -7, -4, -2]))