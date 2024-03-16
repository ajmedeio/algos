class Solution:
    def bfs(self, grid: List[List[str]], i: int, j: int):
        il = len(grid)
        jl = len(grid[0])
        
                
    
    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid) is 0 or len(grid[0]) is 0:
            return 0
        il = len(grid)
        jl = len(grid[0])
        islandCount = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] is "1":
                    islandCount += 1
                    q = [(i,j)]
                    while q:
                        ci, cj = q.pop(0)
                        if ci-1 >= 0 and grid[ci-1][cj] is "1":
                            grid[ci-1][cj] = 0
                            q.append((ci-1,cj))
                        if ci + 1 < il and grid[ci+1][cj] is "1":
                            grid[ci+1][cj] = 0
                            q.append((ci+1,cj))
                        if cj - 1 >= 0 and grid[ci][cj-1] is "1":
                            grid[ci][cj-1] = 0
                            q.append((ci,cj-1))
                        if cj + 1 < jl and grid[ci][cj+1] is "1":
                            grid[ci][cj+1] = 0
                            q.append((ci,cj+1))
                    
                
        return islandCount