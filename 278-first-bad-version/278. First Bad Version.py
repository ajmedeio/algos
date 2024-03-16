# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        lo = 1
        hi = n
        while lo <= hi:
            choice = lo + ((hi - lo) // 2)
            if isBadVersion(choice):
                hi = choice - 1
            else:
                lo = choice + 1
        return lo