class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        n = len(A)
        l, r = 0, n-1
        while l < r:
            if A[l] % 2 == 0:
                l += 1
            elif A[r] % 2 == 1:
                r -= 1
            elif A[l] % 2 == 1 and A[r] % 2 == 0:
                A[l], A[r] = A[r], A[l]
                l += 1
                r -= 1
        return A
