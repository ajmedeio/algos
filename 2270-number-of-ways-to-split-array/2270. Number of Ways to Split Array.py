class Solution:
    def waysToSplitArray(self, A: List[int]) -> int:
        n = len(A)
        out = 0
        P = [A[0]] * n
        for i in range(1, n):
            P[i] = P[i-1] + A[i]
        for i in range(n-1):
            if P[i] >= P[n-1] - P[i]:
                out += 1
        return out