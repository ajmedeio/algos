class Solution:
    def minOperations(self, A: List[int], x: int) -> int:
        n = len(A)
        target = sum(A) - x
        w_max = -math.inf
        s = 0
        l = 0
        for i in range(n):
            s += A[i]
            while l <= i and s > target:
                s -= A[l]
                l += 1
            if s == target:
                w_max = max(w_max, i - l + 1)
        return len(A) - w_max if w_max != -math.inf else -1
