class Solution:
    def removeDuplicates(self, A: List[int]) -> int:
        n = len(A)
        insertion = 1
        for i in range(1, n):
            if A[i] != A[i-1]:
                A[insertion] = A[i]
                insertion += 1
        return insertion
