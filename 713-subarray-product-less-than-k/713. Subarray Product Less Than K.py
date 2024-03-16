class Solution:
    def numSubarrayProductLessThanK(self, A: List[int], k: int) -> int:
        n = len(A)
        p = 1
        out = 0
        l = 0
        for i in range(n):
            p *= A[i]
            while l <= i and p >= k:
                p = p // A[l]
                l += 1
            out += i - l + 1
        return out