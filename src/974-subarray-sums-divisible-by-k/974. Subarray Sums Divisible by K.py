class Solution:
    def subarraysDivByK(self, A: List[int], k: int) -> int:
        n = len(A)
        c = {0: 1}
        out = 0
        p = 0
        for i in range(n):
            p = (p + A[i]) % k
            # how many prefixes add up to the same value % k
            out += c.get(p, 0)
            c[p] = c.get(p, 0) + 1
        return out
