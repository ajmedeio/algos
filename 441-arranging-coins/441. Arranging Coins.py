class Solution:
    def arrangeCoins(self, n: int) -> int:
        n2 = 2 * n
        lo, hi = 0, n2
        while lo <= hi:
            guess = lo + ((hi - lo) >> 1)
            val = guess * guess + guess
            if val < n2:
                lo = guess + 1
            elif val > n2:
                hi = guess - 1
            else:
                return guess
        return hi
