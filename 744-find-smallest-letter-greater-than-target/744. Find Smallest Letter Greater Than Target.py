class Solution:
    def nextGreatestLetter(self, A: List[str], t: str) -> str:
        lo, hi = 0, len(A) - 1
        while lo <= hi:
            p = lo + ((hi - lo) // 2)
            if A[p] > t:
                hi = p - 1
            elif A[p] <= t:
                lo = p + 1
        if lo < len(A):
            return A[lo]
        else:
            return A[0]