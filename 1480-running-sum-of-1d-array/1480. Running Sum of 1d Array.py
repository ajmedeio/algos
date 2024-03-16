class Solution:
    def runningSum(self, A: List[int]) -> List[int]:
        n = len(A)
        out = []
        s = 0
        for i in range(n):
            s += A[i]
            out.append(s)
        return out
