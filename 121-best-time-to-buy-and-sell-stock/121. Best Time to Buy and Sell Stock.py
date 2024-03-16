class Solution:
    def maxProfit(self, P: List[int]) -> int:
        n = len(P)
        P_min = inf
        profit = 0
        for i in range(n):
            P_min = min(P_min, P[i])
            profit = max(profit, P[i] - P_min)
        return profit
