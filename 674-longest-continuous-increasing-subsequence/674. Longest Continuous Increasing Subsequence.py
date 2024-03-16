class Solution:
    def findLengthOfLCIS(self, A: List[int]) -> int:
        l = 0
        c = 0
        n = len(A)
        prev = -math.inf
        for i in range(n):
            if A[i] > prev:
                c += 1
                l = max(c, l)
            else:
                c = 1
            prev = A[i]
        return l
