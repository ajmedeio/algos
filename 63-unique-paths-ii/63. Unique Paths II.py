class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        n = len(grid) if grid is not None else 0
        m = len(grid[0]) if n > 0 else 0
        f = [[0 for _ in range(m)] for _ in range(n)]
        f[0][0] = 1 if grid[0][0] == 0 else 0
        for row in range(1, n):
            f[row][0] = 0 if grid[row][0] == 1 else f[row - 1][0]
        for col in range(1, m):
            f[0][col] = 0 if grid[0][col] == 1 else f[0][col - 1]

        for row in range(1, n):
            for col in range(1, m):
                f[row][col] = 0 if grid[row][col] == 1 else f[row - 1][col] + f[row][col - 1]
        
        return f[-1][-1]
