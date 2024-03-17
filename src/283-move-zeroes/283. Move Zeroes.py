class Solution:
    def moveZeroes(self, A: List[int]) -> None:
        n = len(A)
        i, j = 0, 1
        while j < n:
            if A[i] != 0:
                i += 1
                j = max(j, i+1)
            elif A[j] == 0:
                j += 1
            else:
                A[i], A[j] = A[j], A[i]
                i += 1
                j += 1
