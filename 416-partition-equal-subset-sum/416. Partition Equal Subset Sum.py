class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        total = sum(nums)
        k = total // 2
        max_num = max(nums)
        if total % 2 != 0:
            return False
        if max_num > k:
            return False

        # initialize map where row is index into nums and column is target value from 0 to k+1
        memo = {}
        memo[(0, 0)] = True
        for i in range(1, n):
            memo[(i, 0)] = True

        for t in range(1, k+1):
            memo[(0, t)] = False
        
        def rec(i, t):
            if (i, t) in memo:
                return memo[(i, t)]
            if t < 0 or i < 0:
                return False
            
            memo[(i, t)] = rec(i-1, t-nums[i]) or rec(i-1, t)
            return memo[(i, t)]
        return rec(len(nums)-1, k)
        
        

    # def canPartition(self, nums: List[int]) -> bool:
    #     n = len(nums)
    #     total = sum(nums)
    #     if total % 2 != 0:
    #         return False
        
    #     k = total // 2
    #     f = [[False] * (k+1) for _ in range(n+1)]
    #     f[0][0] = True

    #     for i in range(1, n+1):
    #         for t in range(1, k+1):
    #             f[i][t] = f[i-1][t]  # include case
    #             if t - nums[i-1] >= 0:
    #                 f[i][t] = f[i][t] or f[i-1][t - nums[i-1]]  # exclude case

    #     return f[-1][-1]