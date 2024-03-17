class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        A = nums  # alias for shorter line length
        for i in range(n):
            while i != A[i]:
                dst = A[i]
                if dst == n:
                    break
                A[i], A[dst] = A[dst], A[i]
        for i in range(n):
            if A[i] != i:
                return i
        return n
