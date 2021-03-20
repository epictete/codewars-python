def check_row(row):
    for i in row:
        if row.count(i) > 1:
            return False
    return True

def check_cols(board):
    for i in range(9):
        row = []
        for j in range(9):
            row.append(board[j][i])
        if not check_row(row):
            return False
    return True

def check_blocks(board):
    for i in range(0, 7, 3):
        for j in range(0, 7, 3):
            a = board[i][j:j+3]
            b = board[i+1][j:j+3]
            c = board[i+2][j:j+3]
            if check_row(a + b + c):
                return True
            else:
                return False

def valid_solution(board):
    for i in board:
        if not check_row(i):
            return False
    if not check_cols(board):
        return False
    if not check_blocks(board):
        return False
    return True

print(valid_solution([[5, 3, 4, 6, 7, 8, 9, 1, 2], 
                                   [6, 7, 2, 1, 9, 5, 3, 4, 8],
                                   [1, 9, 8, 3, 4, 2, 5, 6, 7],
                                   [8, 5, 9, 7, 6, 1, 4, 2, 3],
                                   [4, 2, 6, 8, 5, 3, 7, 9, 1],
                                   [7, 1, 3, 9, 2, 4, 8, 5, 6],
                                   [9, 6, 1, 5, 3, 7, 2, 8, 4],
                                   [2, 8, 7, 4, 1, 9, 6, 3, 5],
                                   [3, 4, 5, 2, 8, 6, 1, 7, 9]]))

print(valid_solution([[5, 3, 4, 6, 7, 8, 9, 1, 2], 
                                   [6, 7, 2, 1, 9, 0, 3, 4, 9],
                                   [1, 0, 0, 3, 4, 2, 5, 6, 0],
                                   [8, 5, 9, 7, 6, 1, 0, 2, 0],
                                   [4, 2, 6, 8, 5, 3, 7, 9, 1],
                                   [7, 1, 3, 9, 2, 4, 8, 5, 6],
                                   [9, 0, 1, 5, 3, 7, 2, 1, 4],
                                   [2, 8, 7, 4, 1, 9, 6, 3, 5],
                                   [3, 0, 0, 4, 8, 1, 1, 7, 9]]))