class Solution:
    def wiggleSort(self, A: List[int]) -> None:
        n = len(A)
        for i in range(0, n-1):
            if (i % 2 == 0) == (A[i] > A[i+1]):
                A[i], A[i+1] = A[i+1], A[i]
