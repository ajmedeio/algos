class Solution:
    def searchInsert(self, A: List[int], t: int) -> int:
        lo, hi = 0, len(A) - 1
        while lo <= hi:
            p = lo + ((hi - lo) // 2)
            if A[p] == t:
                return p
            elif A[p] > t:
                hi = p - 1
            else:
                lo = p + 1
        return lo
