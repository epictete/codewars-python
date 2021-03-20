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

def check_squares(board):
    for i in range(0, 7, 3):
        for j in range(0, 7, 3):
            a = board[i][j:j+3]
            b = board[i+1][j:j+3]
            c = board[i+2][j:j+3]
            if check_row(a + b + c):
                return True
            else:
                return False

def done_or_not(board):
    for i in board:
        if not check_row(i):
            return "Try again!"
    if not check_cols(board):
        return "Try again!"
    if not check_squares(board):
        return "Try again!"
    return "Finished!"

print(done_or_not([[1, 3, 2, 5, 7, 9, 4, 6, 8]
                ,[4, 9, 8, 2, 6, 1, 3, 7, 5]
                ,[7, 5, 6, 3, 8, 4, 2, 1, 9]
                ,[6, 4, 3, 1, 5, 8, 7, 9, 2]
                ,[5, 2, 1, 7, 9, 3, 8, 4, 6]
                ,[9, 8, 7, 4, 2, 6, 5, 3, 1]
                ,[2, 1, 4, 9, 3, 5, 6, 8, 7]
                ,[3, 6, 5, 8, 1, 7, 9, 2, 4]
                ,[8, 7, 9, 6, 4, 2, 1, 5, 3]]))

print(done_or_not([[1, 3, 2, 5, 7, 9, 4, 6, 8]
                ,[4, 9, 8, 2, 6, 1, 3, 7, 5]
                ,[7, 5, 6, 3, 8, 4, 2, 1, 9]
                ,[6, 4, 3, 1, 5, 8, 7, 9, 2]
                ,[5, 2, 1, 7, 9, 3, 8, 4, 6]
                ,[9, 8, 7, 4, 2, 6, 5, 3, 1]
                ,[2, 1, 4, 9, 3, 5, 6, 8, 7]
                ,[3, 6, 5, 8, 1, 7, 9, 2, 4]
                ,[8, 7, 9, 6, 4, 2, 1, 3, 5]]))