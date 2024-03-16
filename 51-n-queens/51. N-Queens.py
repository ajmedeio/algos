class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        out, B = [], [['.' for _ in range(n)] for _ in range(n)]
        placed = 0
      
        def next_cell(i, j):
            j = (j+1) % n
            return (i+1, j) if j == 0 else (i,j)

        def is_horizontal_clear(i):
            return 'Q' not in B[i]

        def is_vertical_clear(j):
            return 'Q' not in [B[i][j] for i in range(n)]

        def is_diagonal_clear(i, j):
            r, c = i-1, j-1
            while c >= 0 and r >= 0:
                if 'Q' in B[r][c]:
                    return False
                r -= 1
                c -= 1
            r, c = i - 1, j+1
            while c < n and r >= 0:
                if 'Q' in B[r][c]:
                    return False
                r -= 1
                c += 1
            return True

        def is_valid_placement(i, j):
            return (
                is_horizontal_clear(i)
                and is_vertical_clear(j)
                and is_diagonal_clear(i, j)
            )

        def recurse(i=0, j=0):
            nonlocal placed
            if i >= n or j >= n:
                return
            if is_valid_placement(i, j):
                B[i][j] = 'Q'
                placed += 1
                if placed == n:
                    out.append(copy.deepcopy(B))
                else:
                    recurse(*next_cell(i, j))
                B[i][j] = '.'
                placed -= 1
            recurse(*next_cell(i, j))
        recurse()
        for solution_i in range(len(out)):
            solution = out[solution_i]
            for i in range(len(solution)):
                solution[i] = "".join(solution[i])
        return out
