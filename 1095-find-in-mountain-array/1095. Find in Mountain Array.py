# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, t: int, A: 'MountainArray') -> int:
        n = A.length()
        lo, hi = 1, n-2
        while lo <= hi:
            i = lo + ((hi - lo) // 2)
            c = A.get(i)
            s = A.get(i+1)
            if c < s:
                lo = i + 1
            else:
                hi = i - 1
        # lo is pointing to peak
        peak = lo
        lo, hi = 0, peak
        while lo <= hi:
            i = lo + ((hi - lo) // 2)
            c = A.get(i)
            if t == c:
                return i
            elif c < t:
                lo = i + 1
            else:
                hi = i - 1
        # we didn't find target in left piece
        # iterate over right
        lo, hi = peak+1, n-1
        while lo <= hi:
            i = lo + ((hi - lo) // 2)
            c = A.get(i)
            if c == t:
                return i
            elif c < t:
                hi = i - 1
            else:
                lo = i + 1
        return -1
