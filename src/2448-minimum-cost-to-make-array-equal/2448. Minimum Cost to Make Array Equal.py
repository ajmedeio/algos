class Solution:
    def minCost(self, A: List[int], C: List[int]) -> int:
        n = len(A)
        def calc_cost(target):
            return sum(abs(A[i] - target) * C[i] for i in range(n))

        lo, hi = min(A), max(A)
        while lo <= hi:
            i = lo + ((hi - lo) // 2)
            c1 = calc_cost(i)
            c2 = calc_cost(i+1)
            if c1 > c2:
                lo = i + 1
            else:
                hi = i - 1
        return calc_cost(lo)
