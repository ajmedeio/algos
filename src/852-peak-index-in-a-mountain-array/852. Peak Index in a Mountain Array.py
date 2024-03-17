class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        n = len(A)
        lo, hi = 1, n-2
        while lo <= hi:
            i = lo + ((hi - lo) // 2)
            if A[i-1] < A[i] > A[i+1]:
                return i
            elif A[i-1] < A[i] < A[i+1]:
                lo = i + 1
            else:
                hi = i - 1
        return -1