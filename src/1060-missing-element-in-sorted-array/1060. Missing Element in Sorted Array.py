class Solution:
    def missingElement(self, A: List[int], k: int) -> int:
        n = len(A)
        lo, hi = 0, n - 1
        offset = A[0]
        while lo <= hi:
            i = lo + ((hi - lo) // 2)
            n_missing = A[i] - (offset + i)
            if n_missing >= k:
                hi = i -1
            else:
                lo = i + 1
        return offset + k + hi