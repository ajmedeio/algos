class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        A = [0] + nums + [0]
        n = len(A)
        P = [0] * n
        for i in range(1, n):
            P[i] = P[i-1] + A[i]

        for i in range(1, n-1):
            if P[i-1] == P[n-1] - P[i]:
                return i-1
        return -1
