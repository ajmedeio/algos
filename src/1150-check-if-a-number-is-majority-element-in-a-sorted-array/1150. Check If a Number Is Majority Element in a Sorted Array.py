def search(A, t, left=True):
    lo, hi = 0, len(A) - 1
    while lo <= hi:
        i = lo + ((hi - lo) // 2)
        if A[i] > t or (left and A[i] == t):
            hi = i - 1
        else:
            lo = i + 1
    return lo if left else hi

class Solution:
    def isMajorityElement(self, A: List[int], t: int) -> bool:
        # binary search the left most target occurrence then ask if 
        # leftmost + n/2 + 1 is also the target
        n = len(A)
        start = search(A, t)
        rightmost = start + (n // 2)
        return start < n and rightmost < n and A[rightmost] == t