class Solution:
    def maxProfit(self, k: int, P: List[int]) -> int:
        buy, sell = [inf] * (k+1), [0] * (k+1)
        for i in range(len(P)):
            for j in range(1, k+1):
                buy[j] = min(buy[j], P[i] - sell[j-1])
                sell[j] = max(sell[j], P[i] - buy[j])
        return sell[k]
