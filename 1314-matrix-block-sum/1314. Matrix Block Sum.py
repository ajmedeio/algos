class Solution:
    def matrixBlockSum(self, M: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(M), len(M[0])
        def get(M, i, j):
            if 0 <= i < m and 0 <= j < n:
                return M[i][j]
            else:
                return 0

        P = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                P[i][j] = get(M, i, j) + get(P, i-1, j) + get(P, i, j-1) - get(P, i-1, j-1)
        
        out = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                r1, r2 = max(0, i-k), min(m-1, i+k)
                c1, c2 = max(0, j-k), min(n-1, j+k)
                out[i][j] = get(P, r2, c2) - get(P, r2, c1-1) - get(P, r1-1, c2) + get(P, r1-1, c1-1)
        return out
