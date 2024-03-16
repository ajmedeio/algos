class Solution:
    def twoSum(self, A: List[int], t: int) -> List[int]:
        n = len(A)
        lo, hi = 0, n-1
        while lo < hi:
            c = A[lo] + A[hi]
            if c > t:
                hi -= 1
            elif c < t:
                lo += 1
            else:
                return [lo+1, hi+1]
        return [-1, -1]
