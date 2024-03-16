from math import inf

class Solution:
    def maxProduct2(self, nums: List[int]) -> int:
        r = imin = imax = nums[0]
        for num in nums[1:]:
            candidates = (n, imax * n, imin * n)
            imax = max(candidates)
            imin = min(candidates)
            r = max(r, imax)
        return r

    def maxProduct(self, nums: list[int]) -> int:
        global_max = -inf

        for i in range(len(nums)):
            curr_prod = nums[i]
            global_max = max(global_max, curr_prod)
            for j in range(i + 1, len(nums)):
                curr_prod *= nums[j]
                global_max = max(global_max, curr_prod)

        return global_max
