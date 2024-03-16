class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        if len(costs) == 0:
            return 0
        if len(costs) == 1:
            return min(costs[0])
            
        f = [[0 for _ in range(3)] for _ in range(len(costs))]

        for color in range(3):
            f[0][color] = costs[0][color]
        
        for h_i in range(len(costs)):
            for c_i in range(3):
                f[h_i][c_i] = min(f[h_i-1][c_i-1], f[h_i-1][(c_i+1) % 3]) + costs[h_i][c_i]
        
        return min(f[-1])