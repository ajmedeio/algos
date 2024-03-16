class Solution:
    def maxSubArrayLen(self, A: List[int], k: int) -> int:
        n = len(A)
        c = {0: 0}
        out = 0
        p = 0
        for i in range(n):
            p = p + A[i]
            out = max(out, i+1 - c.get(p-k, inf))
            if p not in c:
                c[p] = i+1
        return out
