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
    def searchRange(self, A: List[int], t: int) -> List[int]:
        start, end = search(A, t, True), search(A, t, False)
        return [start, end] if start <= end else [-1, -1]
