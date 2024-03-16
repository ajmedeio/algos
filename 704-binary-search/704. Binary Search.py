class Solution:
    def search(self, A: List[int], target: int) -> int:
        n = len(A)
        l = 0
        r = n - 1
        while l <= r:
            mid = (l + r) // 2
            if A[mid] == target:
                return mid
            elif A[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return -1
