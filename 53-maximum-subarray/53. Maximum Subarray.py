class Solution:
    def maxSubArray(self, A: List[int]) -> int:
        n = len(A)
        m, p = -inf, 0
        for i in range(0, n):
            p = max(p + A[i], A[i])
            m = max(m, p)
        return m
