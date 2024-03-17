class Solution:
    # this is a catalan trees problem, aka matrix chain multiplication
    # and we need to maximize the chain instead of minimizing the chain
    def maxCoins(self, nums: List[int]) -> int:
        balloons = [1] + nums + [1]
        n = len(balloons)
        f = [[0 for _ in range(n)] for _ in range(n)]

        # base cases for f are 0 on the diagonal of the solution matrix
        # technically this isn't necessary because we default all cells to zero
        for i in range(n):
            for j in range(i+1):
                f[i][j] = 0

        for i in range(n-2, -1, -1):
            for j in range(i+1, n):
                for k in range(i+1, j):
                    f[i][j] = max(
                        f[i][j], 
                        f[i][k] + f[k][j] + balloons[i] * balloons[k] * balloons[j]
                    )

        return f[0][n-1]
