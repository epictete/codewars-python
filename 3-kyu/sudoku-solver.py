solution = [[5,3,4,6,7,8,9,1,2],
            [6,7,2,1,9,5,3,4,8],
            [1,9,8,3,4,2,5,6,7],
            [8,5,9,7,6,1,4,2,3],
            [4,2,6,8,5,3,7,9,1],
            [7,1,3,9,2,4,8,5,6],
            [9,6,1,5,3,7,2,8,4],
            [2,8,7,4,1,9,6,3,5],
            [3,4,5,2,8,6,1,7,9]]

puzzle = [[5,3,0,0,7,0,0,0,0],
          [6,0,0,1,9,5,0,0,0],
          [0,9,8,0,0,0,0,6,0],
          [8,0,0,0,6,0,0,0,3],
          [4,0,0,8,0,3,0,0,1],
          [7,0,0,0,2,0,0,0,6],
          [0,6,0,0,0,0,2,8,0],
          [0,0,0,4,1,9,0,0,5],
          [0,0,0,0,8,0,0,7,9]]

def check(y, x, n, puzzle):
    for i in range(9):
        if puzzle[y][i] == n:
            return False
    for i in range(9):
        if puzzle[i][x] == n:
            return False
    boxX = (x//3)*3
    boxY = (y//3)*3
    for i in range(3):
        for j in range(3):
            if puzzle[boxY+i][boxX+j] == n:
                return False
    return True

def sudoku(puzzle):
    for y in range(9):
        for x in range(9):
            if puzzle[y][x] == 0:
                for n in range(1, 10):
                    if check(y, x, n, puzzle):
                        puzzle[y][x] = n
                        if sudoku(puzzle):
                            return puzzle
                        puzzle[y][x] = 0
                return
    return puzzle

print(sudoku(puzzle))
print(sudoku(puzzle) == solution)