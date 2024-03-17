class Solution:
    def getModifiedArray(self, n: int, U: List[List[int]]) -> List[int]:
        A = [0] * n
        for s, e, v in U:
            A[s] += v
            if e + 1 < n:
                A[e+1] -= v
        for i in range(1, n):
            A[i] += A[i-1]
        return A