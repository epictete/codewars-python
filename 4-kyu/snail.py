def switch(arr):
    res = []
    for i in range(len(arr[0])):
        row = []
        for j in range(len(arr)):
            row.append(arr[j][i])
        res.append(row)
    res.reverse()
    return res

def snail(arr):
    res = []
    for i in arr[0]:
        res.append(i)
    if arr[1:]:
        return res + snail(switch(arr[1:]))
    else:
        return arr[0]


arr = [[1,2,3],
       [4,5,6],
       [7,8,9]]

print(snail(arr))