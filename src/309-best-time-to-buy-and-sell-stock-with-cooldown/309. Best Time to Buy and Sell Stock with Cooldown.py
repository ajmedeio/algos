class Solution:
    def maxProfit(self, P: List[int]) -> int:
        G = [0] * 4
        f = 0
        for i in range(1, len(P)):
            f = P[i] - P[i-1] + max(G[(i-3) % 4], f)
            G[i % 4] = max(G[(i-1) % 4], f)
        return G[(len(P)-1) % 4]