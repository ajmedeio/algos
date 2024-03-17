class Solution:
    def subarraySum(self, A: List[int], k: int) -> int:
        n = len(A)
        p = 0
        c = {0: 1}
        out = 0
        for i in range(n):
            p += A[i]
            out += c.get(p - k, 0)
            c[p] = c.get(p, 0) + 1
        return out
