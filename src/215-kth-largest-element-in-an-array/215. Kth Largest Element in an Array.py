def partition(A, lo, hi):
    p = random.randint(lo, hi)
    v = A[p]
    A[p], A[lo] = A[lo], A[p]
    lt, i, gt = lo, lo, hi
    while i <= gt:
        if A[i] > v:
            A[i], A[gt] = A[gt], A[i]
            gt -= 1
        elif A[i] < v:
            A[i], A[lt] = A[lt], A[i]
            lt += 1
        elif A[i] == v:
            i += 1
    return lt, gt  # these pointers now lie on the left and right edge of the equal section


class Solution:
    def findKthLargest(self, A: List[int], k: int) -> int:
        n = len(A)
        lo, hi = 0, n-1
        while True:
            l, r = partition(A, lo, hi)
            if l <= (n-k) <= r:
                return A[l]
            elif l < (n-k) and r < (n-k):
                lo = r+1
            elif (n-k) < l and (n-k) < r:
                hi = l-1
