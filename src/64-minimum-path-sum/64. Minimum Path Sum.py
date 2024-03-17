class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if grid is None or len(grid) == 0:
            return 0

        # init our answers matrix
        n = len(grid)
        m = len(grid[0]) if n > 0 else 0
        f = [[0 for _ in range(m)] for _ in range(n)]
        
        # base cases
        f[0][0] = grid[0][0]
        for row in range(1, n):
            f[row][0] = f[row-1][0] + grid[row][0]
        for col in range(1, m):
            f[0][col] = f[0][col-1] + grid[0][col]

        # bottom up tabulation
        for row in range(1, n):
            for col in range(1, m):
                f[row][col] = min(f[row-1][col], f[row][col-1]) + grid[row][col]
        
        row, col = n-1, m-1
        min_path = [(row,col)]
        while (row, col) != (0, 0):
            if row - 1 < 0:
                min_path.insert(0, (row, col-1))
                row, col = row, col-1
            elif col - 1 < 0:
                min_path.insert(0, (row-1, col))
                row, col = row-1, col
            elif f[row-1][col] <= f[row][col-1]:
                min_path.insert(0, (row-1, col))
                row, col = row-1, col
            else:
                min_path.insert(0, (row, col-1))
                row, col = row, col-1

        print(min_path)
        return f[-1][-1]
