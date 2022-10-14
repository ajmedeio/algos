def no_queens_vertically(slate, i, j):
    for row in range(len(slate)):
        if slate[row][j] == 'q':
            return False
    return True


def no_queens_diagonally(slate, i, j, n):
    # how do we get the diagonals
    # we need to start at i,j and grab all [i-1][j-1], [i-1][j+1], [i+1][j-1], [i+1][j+1]
    t_i, t_j = i, j
    while t_i > 0 and t_j > 0:
        t_i -= 1
        t_j -= 1
        if slate[t_i][t_j] == 'q':
            return False
    t_i, t_j = i, j
    while t_i > 0 and t_j < n - 1:
        t_i -= 1
        t_j += 1
        if slate[t_i][t_j] == 'q':
            return False
    return True


def find_all_arrangements(n):
    out = []  # list of lists of strings
    slate = [['-' for _ in range(n)] for _ in range(n)]  # initialize 2-d array of dashes

    def rec(row):
        if row == n:
            output_slate = ['' for _ in range(n)]
            for row in range(n):
                for col in range(n):
                    output_slate[row] += slate[row][col]
            out.append(output_slate)
            return

        # possible choices to make?
        # we can either place the queen or we can't
        # what determines if we can place the queen?
        for col in range(n):
            if no_queens_vertically(slate, row, col) and no_queens_diagonally(slate, row, col, n):
                slate[row][col] = 'q'
                rec(row + 1)
                slate[row][col] = '-'

    rec(0)
    return out


if __name__ == '__main__':
    for arrangement in find_all_arrangements(4):
        for row in arrangement:
            print(row)
        print('end arrangement')
