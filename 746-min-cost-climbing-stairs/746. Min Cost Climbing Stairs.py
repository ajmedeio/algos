class Solution:
    def minCostClimbingStairs(self, C: List[int]) -> int:
        n = len(C)
        F = [0] * 2
        F[0] = C[0]
        F[1] = C[1]
        for i in range(2, n):
            F[i%2] = min(F[(i-1)%2], F[(i-2)%2]) + C[i]
        return min(F)
