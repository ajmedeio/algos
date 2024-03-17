class Solution:
    def minEatingSpeed(self, P: List[int], h: int) -> int:
        n = len(P)
        lo, hi = 1, max(P)
        while lo <= hi:
            i = lo + ((hi - lo) >> 1)
            h_a = 0
            for j in range(n):
                h_a += ceil(P[j] / i)
            if h_a > h:
                lo = i + 1
            elif h_a <= h:
                hi = i - 1
        return lo
