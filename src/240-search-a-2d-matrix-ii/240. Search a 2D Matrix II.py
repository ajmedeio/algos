class Solution:
    def searchMatrix(self, M: List[List[int]], t: int) -> bool:
        if len(M) == 0 or len(M[0]) == 0:
            return False

        m, n = len(M), len(M[0])
        row, col = m - 1, 0
        while col < n and row >= 0:
            if M[row][col] > t:
                row -= 1
            elif M[row][col] < t:
                col += 1
            else:
                return True
        return False
