class Solution:
    def findMin(self, A: List[int]) -> int:
        n = len(A)
        if n == 1:
            return A[0]
        if A[0] < A[n-1]:
            return A[0]

        lo, hi = 0, n-1
        while lo <= hi:
            i = lo + ((hi - lo) // 2)
            if A[i] < A[0]:
                hi = i - 1
            else:
                lo = i + 1
        return A[lo]
