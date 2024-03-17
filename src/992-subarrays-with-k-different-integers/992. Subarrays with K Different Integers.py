def decrement(c: Counter, val: int):
    c[val] -= 1
    if c[val] == 0:
        del c[val]

class Solution:
    def subarraysWithKDistinct(self, A: List[int], k: int) -> int:
        n = len(A)
        l = 0
        ll = 0
        out = 0
        c1 = Counter()
        c2 = Counter()
        for i in range(n):
            c1[A[i]] += 1
            c2[A[i]] += 1
            while len(c1) >= k:
                decrement(c1, A[l])
                l += 1
            while len(c2) > k:
                decrement(c2, A[ll])
                ll += 1
            out += l - ll
        return out