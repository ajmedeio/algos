class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        A = nums
        n = len(A)
        for i in range(n):
            while A[i] != i + 1:
                d = A[i] - 1
                if A[d] == A[i]:
                    break
                A[i], A[d] = A[d], A[i]
        for i in range(n):
            if A[i] != i+1:
                return [nums[i], i+1]