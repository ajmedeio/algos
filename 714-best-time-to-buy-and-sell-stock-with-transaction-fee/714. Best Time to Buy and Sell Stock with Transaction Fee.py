class Solution:
    def maxProfit(self, P: List[int], fee: int) -> int:
        s, f = -fee, 0
        for i in range(1, len(P)):
            s = P[i] - P[i-1] + max(s, f - fee)
            f = max(f, s)
        return f
