if __name__ == '__main__':
    def horizontally_valid(board, i, _j, c):
        for col in range(0, 9):
            if c == board[i][col]:
                return False
        return True


    def vertically_valid(board, _i, j, c):
        for row in range(0, 9):
            if c == board[row][j]:
                return False
        return True


    def locally_valid(board, i, j, c):  # i.e. 5,2
        # think, how do we look up the local square of cells without enumerating them all?
        local_row = i // 3  # 1
        local_col = j // 3  # 0
        start_row = local_row * 3  # 3
        start_col = local_col * 3  # 0
        for row in range(start_row, start_row + 3):  # 3 to 6 = 3, 4, 5
            for col in range(start_col, start_col + 3):  # 0 to 3 = 0, 1, 2
                if c == board[row][col]:
                    return False
        return True


    def is_valid_play(board, i, j, c):
        h = horizontally_valid(board, i, j, c)
        v = vertically_valid(board, i, j, c)
        l = locally_valid(board, i, j, c)
        return h and v and l


    def solve_sudoku_puzzle(board: list[list[int]]):
        def rec(i, j):
            if i == 9:
                return True

            if board[i][j] == 0:
                for c in range(1, 10):
                    if is_valid_play(board, i, j, c):
                        board[i][j] = c
                        solved = rec(i, j + 1) if j + 1 < 9 else rec(i + 1, 0)
                        if solved:
                            return True
                        else:
                            board[i][j] = 0
            else:
                return rec(i, j + 1) if j + 1 < 9 else rec(i + 1, 0)

        rec(0, 0)
        return board

    for row in solve_sudoku_puzzle([
        [8, 4, 9, 0, 0, 3, 5, 7, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 0],
        [7, 0, 0, 0, 9, 0, 0, 8, 3],
        [0, 0, 0, 9, 4, 6, 7, 0, 0],
        [0, 8, 0, 0, 5, 0, 0, 4, 0],
        [0, 0, 6, 8, 7, 2, 0, 0, 0],
        [5, 7, 0, 0, 1, 0, 0, 0, 4],
        [0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 2, 1, 7, 0, 0, 8, 6, 5]
    ]):
        print(row)

