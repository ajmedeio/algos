class Solution:
    def findMin(self, A: List[int]) -> int:
        n = len(A)
        a0 = 0
        for i in range(n-1):
            if A[i] < A[-1]:
                return A[i]
            elif A[i] > A[-1]:
                a0 = i
                break
        else:
            return A[0]
        
        A0 = A[a0]
        lo, hi = a0+1, n-1
        while lo <= hi:
            i = lo + ((hi - lo) // 2)
            if A[i] < A0:
                hi = i - 1
            else:
                lo = i + 1
        return A[lo]
