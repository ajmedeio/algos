class Solution:
    def missingNumber(self, A: List[int]) -> int:
        n = len(A)
        increment = min(A[1] - A[0], A[2] - A[1])
        offset = A[0]
        lo, hi = 0, n - 1
        while lo <= hi:
            i = lo + ((hi - lo) // 2)
            expected = increment * i + offset
            if A[i] == expected:
                lo = i + 1
            else:
                hi = i - 1
        return A[lo] - increment if lo < n else A[0]
