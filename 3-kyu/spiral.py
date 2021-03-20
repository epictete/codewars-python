def spiralize(size):
    spiral = [[1 for i in range(size)] for j in range(size)]
    top = 1
    left = 0
    bottom = right = size - 1
    direction = 0

    while left <= right and top <= bottom:
        if direction == 0:
            for i in range(left, right):
                spiral[top][i] = 0
            top += 1
            right -= 1
        elif direction == 1:
            for i in range(top, bottom):
                spiral[i][right] = 0
            right -= 1
            bottom -= 1
        elif direction == 2:
            for i in range(right, left, -1):
                spiral[bottom][i] = 0
            bottom -= 1
            left += 1
        elif direction == 3:
            for i in range(bottom, top, -1):
                spiral[i][left] = 0
            left += 1
            top += 1
        direction = (direction + 1) % 4

    return spiral


for row in spiralize(5):
    print(row)
print(spiralize(5) == [[1, 1, 1, 1, 1], [0, 0, 0, 0, 1], [1, 1, 1, 0, 1], [1, 0, 0, 0, 1], [1, 1, 1, 1, 1]])
for row in spiralize(8):
    print(row)
print(spiralize(8) == [[1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 1, 1, 0, 1],
                       [1, 0, 0, 0, 0, 1, 0, 1], [1, 0, 1, 0, 0, 1, 0, 1], [1, 0, 1, 1, 1, 1, 0, 1],
                       [1, 0, 0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 1, 1, 1, 1]])
