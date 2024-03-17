class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        memo = {}
        n = len(nums)
        c = nums
        def f(t):
            if t in memo:
                return memo[t]
            if t == 0:
                return 1
            
            result = 0
            for i in range(n):
                if t - c[i] >= 0:
                    result += f(t - c[i])
            memo[t] = result
            return result
        return f(target)

    def combinationSum4Tabular(self, nums: List[int], target: int) -> int:
        f = [0] * (target + 1)
        f[0] = 1
        c = nums
        n = len(nums)

        for i in range(1, target + 1):
            for j in range(n):
                if i - c[j] >= 0:
                    f[i] += f[i - c[j]]
        
        return f[-1]