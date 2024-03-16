class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        lo = 0
        hi = n
        out = [0] * (2 * n)
        for i in range(2 * n):
            if i % 2 == 0:
                out[i] = nums[lo]
                lo += 1
            else:
                out[i] = nums[hi]
                hi += 1
        return out
