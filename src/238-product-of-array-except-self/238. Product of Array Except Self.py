class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        L = [0] * n
        R = [0] * n
        L[0], R[-1] = 1, 1

        for i in range(1, n):
            L[i] = L[i-1] * nums[i-1]
        for i in range(n-2, -1, -1):
            R[i] = R[i+1] * nums[i+1]
        out = [0] * n
        for i in range(n):
            out[i] = L[i] * R[i]
        return out