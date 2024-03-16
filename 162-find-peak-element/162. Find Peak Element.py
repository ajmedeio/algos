class Solution:
    def findPeakElement(self, A: List[int]) -> int:
        n = len(A)
        lo, hi = 0, n-1
        while lo <= hi:
            i = lo + ((hi - lo) // 2)
            p = A[i-1] if i-1 >= 0 else -math.inf
            s = A[i+1] if i + 1 < n else -math.inf
            if p < A[i] > s:
                return i
            elif p < A[i]:
                lo = i + 1
            else:
                hi = i - 1
        return -1