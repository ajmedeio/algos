class Solution:
    def minimumReplacement(self, A: List[int]) -> int:
        n = len(A)
        splits = 0
        ahead = A[-1]
        for i in range(n-2, -1, -1):
            if A[i] <= ahead:
                ahead = A[i]
                continue
            chunks = ceil(A[i] / ahead)
            ahead = A[i] // chunks
            splits += chunks - 1
        return splits
