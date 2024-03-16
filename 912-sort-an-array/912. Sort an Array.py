def three_partition(A, lo, hi):
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
            i += 1
        elif A[i] == v:
            i += 1
    return lt, gt  # these pointers now lie on the left and right edge of the equal section

def quicksort(A, lo, hi):
    if lo > hi:
        return
    lt, gt = three_partition(A, lo, hi)
    quicksort(A, lo, lt-1)
    quicksort(A, gt+1, hi)

class Solution:
    def sortArray(self, A: List[int]) -> List[int]:
        quicksort(A, 0, len(A)-1)
        return A