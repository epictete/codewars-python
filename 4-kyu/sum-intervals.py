def sum_of_intervals(intervals):
    
    intervals.sort()
    stack = []
    res = 0

    for i in intervals:
        if len(stack) == 0:
            stack.append(i)
        else:
            if stack[-1][1] > i[0]:
                if stack[-1][1] > i[1]:
                    continue
                else:
                    prev = stack.pop()
                    stack.append([prev[0], i[1]])
            else:
                stack.append(i)
    
    for j in stack:
        res += (j[1] - j[0])

    return res




print(sum_of_intervals([(1, 5)]), 4)
print(sum_of_intervals([(1, 5), (6, 10)]), 8)
print(sum_of_intervals([(1, 5), (1, 5)]), 4)
print(sum_of_intervals([(1, 4), (7, 10), (3, 5)]), 7)
print(sum_of_intervals([(3, 5), (2, 4), (2, 7), (4, 6)]), 5)