class Solution:
    def maxScore(self, A: List[int], k: int) -> int:
        n = len(A)
        l = n - k # we want a window of length 4
        w_min = w = sum(A[0:l])

        for i in range(l, n):
            w -= A[i-l]
            w += A[i]
            w_min = min(w_min, w)
        return sum(A) - w_min
