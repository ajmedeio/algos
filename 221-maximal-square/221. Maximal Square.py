class Solution:
    def maximalSquare(self, M: List[List[str]]) -> int:
        m, n = len(M), len(M[0])
        F = [[0] * n for _ in range(m)]
        out = 0
        for i in range(m):
            F[i][0] = int(M[i][0])
            out = max(out, F[i][0])

        for j in range(n):
            F[0][j] = int(M[0][j])
            out = max(out, F[0][j])
        
        for i in range(1, m):
            for j in range(1, n):
                m = min(F[i-1][j], F[i][j-1], F[i-1][j-1])
                if int(M[i][j]) == 1:
                    F[i][j] = m + 1
                    out = max(out, F[i][j])
                else:
                    F[i][j] = 0
        return out * out
