class Solution:
    def findMaxLength(self, A: List[int]) -> int:
        c = {0: 0}
        n = len(A)
        out = 0
        excess = 0
        for i in range(n):
            if A[i] == 1:
                excess += 1
            else:
                excess -= 1
            out = max(out, i+1 - c.get(excess, inf))
            if excess not in c:
                c[excess] = i + 1
        return out