class Solution:
    def findClosestElements(self, A: List[int], k: int, x: int) -> List[int]:
        n = len(A)
        i_min = bisect_left(A, x)
        i, j = i_min-1, i_min
        while j-i-1 < k:
            if i < 0:
                j += 1
                continue
            
            if j == n or abs(A[i]-x) <= abs(A[j]-x):
                i -= 1
            else:
                j += 1
        return A[i+1:j]
