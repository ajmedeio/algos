class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        out = [[0] * n for _ in range(m)]
        for i in range(m):
            out[i][0] = 1
        for j in range(n):
            out[0][j] = 1

        for i in range(1, m):
            for j in range(1, n):
                out[i][j] = out[i-1][j] + out[i][j-1]        
        return out[-1][-1]