class Solution:
    def matrixSumQueries(self, n: int, queries: List[List[int]]) -> int:
        R = [False] * n
        C = [False] * n
        r, c = n, n
        total = 0
        for t, i, v in reversed(queries):
            if t == 0:  # operate on row, subtract row
                if R[i]:
                    continue
                total += c * v
                R[i] = True
                r -= 1
            elif t == 1:  # operate on row, subtract col
                if C[i]:
                    continue
                total += r * v
                C[i] = True
                c -= 1
        return total