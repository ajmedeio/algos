class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        A = nums
        for i in range(n):
            while A[i] != i+1:
                d = A[i] - 1
                if (d < 0 or d > n-1) or (A[d] == A[i]):
                    break
                A[i], A[d] = A[d], A[i]
        
        for i in range(n):
            if A[i] != i+1:
                return i+1
        return n+1