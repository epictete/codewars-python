def dbl_linear(n):
    u = [1]
    x = y = 0
    for i in range(n):
        newX = 2 * u[x] + 1
        newY = 3 * u[y] + 1
        if newX <= newY:
            u.append(newX)
            x += 1
            if newX == newY:
                y += 1
        else:
            u.append(newY)
            y += 1
    return u[n]


print(dbl_linear(10), 22)
print(dbl_linear(20), 57)
print(dbl_linear(30), 91)
print(dbl_linear(50), 175)