class Solution:
    def search(self, A: List[int], t: int) -> bool:
        n = len(A)
        if n == 1:
            return t == A[0]
        
        first = 0
        while first < n and A[first] == A[n-1]:
            first += 1
        if first == n:  # all elements are duplicates
            return t == A[0]
        
        lo, hi = first, n - 1
        while lo <= hi:
            i = lo + ((hi - lo) // 2)
            if A[i] == t:
                return True
            elif A[i] >= A[lo]:
                if A[lo] <= t < A[i]:
                    hi = i - 1
                else:
                    lo = i + 1
            else:
                if A[i] < t <= A[hi]:
                    lo = i + 1
                else:
                    hi = i - 1
        return False
