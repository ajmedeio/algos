def to_matrix_indices(i, m):
    return i // m, i % m

class Solution:
    def searchMatrix(self, A: List[List[int]], t: int) -> bool:
        n = len(A)
        m = len(A[0])
        # binary search with wrap-around indices
        # need a transformation function to map index to matrix index
        lo, hi = 0, (n * m) - 1
        while lo <= hi:
            i = lo + ((hi - lo) // 2)
            row, col = to_matrix_indices(i, m)
            if A[row][col] == t:
                return True
            elif A[row][col] > t:
                hi = i - 1
            else:
                lo = i + 1
        return False