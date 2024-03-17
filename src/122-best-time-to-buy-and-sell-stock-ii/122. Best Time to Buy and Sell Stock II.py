class Solution:
    def maxProfit(self, P: List[int]) -> int:
        return sum(max(0, P[i] - P[i-1]) for i in range(1, len(P)))