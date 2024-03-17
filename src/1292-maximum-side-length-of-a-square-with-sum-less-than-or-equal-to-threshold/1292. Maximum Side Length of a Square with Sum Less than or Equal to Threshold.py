class Solution:
    def maxSideLength(self, M: List[List[int]], threshold: int) -> int:
        n, m = len(M), len(M[0])
        msl = 0
        P = [[0] * (m+1) for _ in range(n+1)]
        for i in range(n):
            for j in range(m):
                P[i+1][j+1] = M[i][j] + P[i][j+1] + P[i+1][j] - P[i][j]
                if min(i, j) - msl >= 0:
                    partial_sum = P[i+1][j+1] - P[i-msl][j+1] - P[i+1][j-msl] + P[i-msl][j-msl]
                    if partial_sum <= threshold:
                        msl += 1
        return msl
