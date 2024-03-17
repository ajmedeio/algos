class Solution:
    def search(self, A: 'ArrayReader', t: int) -> int:
        hi_i = (2 ** 31) - 1
        lo, hi = 0, hi_i
        while lo <= hi:
            i = lo + ((hi - lo) // 2)
            v = A.get(i)
            if v == t:
                return i
            elif v > t:
                hi = i - 1
            else:
                lo = i + 1
        return -1
