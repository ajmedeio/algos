class Solution:
    def minSubArrayLen(self, t: int, A: List[int]) -> int:
        n = len(A)
        w_sum = 0
        out = math.inf
        l = 0

        for r in range(0, n):
            w_sum += A[r]

            while l <= r and w_sum >= t:
                out = min(out, r - l + 1)
                w_sum -= A[l]
                l += 1
        
        return 0 if out == math.inf else out

