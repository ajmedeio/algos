class Solution:
    def singleNonDuplicate(self, A: List[int]) -> int:
        n = len(A)
        if n == 1:
            return A[0]
        if A[0] != A[1]:
            return A[0]
        if A[n-1] != A[n-2]:
            return A[n-1]
        lo, hi = 1, len(A) - 2
        while lo <= hi:
            i = lo + ((hi - lo) // 2)
            if A[i] != A[i-1] and A[i] != A[i+1]:
                return A[i]
            elif (i % 2 == 0 and A[i] == A[i+1]) or (i % 2 == 1 and A[i] == A[i-1]):
                lo = i + 1
            else:
                hi = i - 1
        return -1