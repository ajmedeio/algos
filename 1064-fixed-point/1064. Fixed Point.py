class Solution:
    def fixedPoint(self, A: List[int]) -> int:
        n = len(A)
        lo, hi = 0, n - 1
        while lo <= hi:
            i = lo + ((hi - lo) // 2)
            if A[i] >= i:
                hi = i - 1
            else:
                lo = i + 1
        return lo if lo < n and A[lo] == lo else -1