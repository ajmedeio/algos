class Solution:
    def isPerfectSquare(self, x: int) -> bool:
        lo, hi = 1, x
        while lo <= hi:
            i = lo + ((hi - lo) >> 1)
            i2 = i * i
            if i2 < x:
                lo = i + 1
            elif i2 > x:
                hi = i - 1
            else:
                return True
        return False