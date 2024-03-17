class Solution:
    def findMedianSortedArrays(self, A: List[int], B: List[int]) -> float:
        def get(A, i):
            if i < 0:
                return -inf
            elif i >= len(A):
                return +inf
            else:
                return A[i]

        m, n, t = len(A), len(B), len(A) + len(B)
        k = t // 2 + 1 if t % 2 == 1 else t // 2
        lo, hi = 0, m-1
        median, successor = None, None
        while lo <= hi:
            i = lo + ((hi - lo) // 2)
            nl = k - i - 1
            if get(B, nl-1) < get(A, i) > get(B, nl):
                hi = i - 1
            elif get(B, nl-1) > get(A, i) < get(B, nl):
                lo = i + 1
            elif get(B, nl-1) <= get(A, i) <= get(B, nl):
                median = A[i]
                successor = min(get(A, i+1), get(B, nl))
                break
        
        if median is None:  # median in B
            nl = k - lo - 1
            median = B[nl]
            if t % 2 == 0:
                successor = min(get(A, lo), get(B, nl+1))

        if t % 2 == 0:
            median = (median + successor) / 2
        return median
