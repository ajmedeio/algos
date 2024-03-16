class Solution:
    def maxScoreSightseeingPair(self, S: List[int]) -> int:
        n = len(S)
        l = S[0]
        f = 0
        for j in range(1, n):
            f = max(f, S[j] + l - j)
            l = max(l, S[j] + j)
        return f
