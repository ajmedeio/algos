def binary_search(A, lo, hi, t):
    while lo <= hi:
        i = lo + ((hi - lo) // 2)
        if A[i] == t:
            return i, lo, hi
        elif A[i] > t:
            hi = i - 1
        else:
            lo = i + 1
    return -1, lo, hi

class Solution:
    def search(self, A: List[int], t: int) -> int:
        n = len(A)
        if A[0] < A[-1]:
            return binary_search(A, 0, n-1, t)[0]
        
        A0 = A[0]
        lo, hi = 1, n-1
        while lo <= hi:
            i = lo + ((hi - lo) // 2)
            if A[i] > A0:
                lo = i + 1
            else:
                hi = i - 1
        left_lo, left_hi, right_lo, right_hi = 0, hi, lo, n-1
        if t < A0:
            return binary_search(A, right_lo, right_hi, t)[0]
        else:
            return binary_search(A, left_lo, left_hi, t)[0]
