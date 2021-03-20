def sweeper(bombs, rows, cols):

    field = [[0 for i in range(cols)] for j in range(rows)]

    for bomb in bombs:
        bomb_row, bomb_col = bomb
        field[bomb_row][bomb_col] = -1

        for i in range(bomb_col - 1, bomb_col + 2):
            for j in range(bomb_row - 1, bomb_row + 2):
                if 0 <= i < cols and 0 <= j < rows and field[j][i] != -1:
                    field[j][i] += 1

    return field


for i in sweeper([[0, 0], [1, 2]], 3, 4):
    print(i)
