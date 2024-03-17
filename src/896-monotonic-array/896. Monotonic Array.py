class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        n = len(A)
        if A[0] <= A[-1]:
            for i in range(n-1):
                if A[i] > A[i+1]:
                    return False
        else:
            for i in range(n-1):
                if A[i] < A[i+1]:
                    return False
        return True
