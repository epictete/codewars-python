def max_sequence(arr):
    maxi = 0
    for i in range(len(arr)):
        for j in range(len(arr)):
            x = arr[i:j+1]
            if len(x) != 0 and sum(x) > maxi:
                maxi = sum(x)
    return maxi



print(max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]))