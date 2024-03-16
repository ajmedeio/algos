class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 1:
            return x
        lo, hi = 0, x // 2
        while lo <= hi:
            i = lo + ((hi - lo) // 2)
            i2 = i * i
            if i2 == x:
                return i
            elif i2 > x:
                hi = i - 1
            else:
                lo = i + 1
        return hi