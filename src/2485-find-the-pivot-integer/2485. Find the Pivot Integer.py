class Solution:
    def pivotInteger(self, n: int) -> int:
        candidate = sqrt(((n*n) + n) / 2)
        if candidate.is_integer():
            return int(candidate)
        else:
            return -1