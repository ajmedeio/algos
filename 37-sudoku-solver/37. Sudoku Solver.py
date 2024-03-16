def submatrix(B, i, j):
    rs = i // 3
    cs = j // 3
    sm = []
    for r in range(0, 3):
        for c in range(0, 3):
            sm.append(B[r + (rs*3)][c + (cs*3)])
    return sm

def new_row_caches(B):
    out = [set()] * 9
    for i in range(9):
        out[i] = set(B[i][:])
    return out

def new_col_caches(B):
    out = [set()] * 9
    for j in range(9):
        out[j] = set([B[i][j] for i in range(9)])
    return out

def new_submatrix_caches(B):
    out = [[set() for _ in range(3)] for _ in range(3)]
    for i in range(3):
        for j in range(3):
            out[i][j] = set(submatrix(B, i*3, j*3))
    return out

def cache_choice(i, j, k, row_caches, col_caches, sub_caches):
    row_caches[i].add(k)
    col_caches[j].add(k)
    sub_caches[i//3][j//3].add(k)

def evict_choice(i, j, k, row_caches, col_caches, sub_caches):
    row_caches[i].remove(k)
    col_caches[j].remove(k)
    sub_caches[i//3][j//3].remove(k)

def is_valid(i, j, k, row_caches, col_caches, sub_caches):
    return (
        k not in row_caches[i]
        and k not in col_caches[j]
        and k not in sub_caches[i//3][j//3]
    )

def next_cell(i, j):
    j = (j+1) % 9
    return (i+1, j) if j == 0 else (i, j)

class Solution:
    def solveSudoku(self, B: List[List[str]]) -> None:
        n, m = len(B), len(B[0])
        if not (n == m == 9):
            return B
        row_caches = new_row_caches(B)
        col_caches = new_col_caches(B)
        sub_caches = new_submatrix_caches(B)

        solved = False
        
        def recurse(i, j):
            nonlocal solved
            if solved:
                return
            if i == n:
                solved = True
                return
            if B[i][j] != '.':
                recurse(*next_cell(i, j))
                return
            for k in range(1, 10):
                l = str(k)
                if is_valid(i, j, l, row_caches, col_caches, sub_caches):
                    B[i][j] = l
                    cache_choice(i, j, l, row_caches, col_caches, sub_caches)
                    recurse(*next_cell(i, j))
                    if not solved:
                        evict_choice(i, j, l, row_caches, col_caches, sub_caches)
                        B[i][j] = '.'
        recurse(0, 0)
        return B
