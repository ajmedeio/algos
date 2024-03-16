class Solution:
    def canJump(self, nums: List[int]) -> bool:
        made_it = [False for _ in range(len(nums))]
        made_it[-1] = True
        for i in range(len(nums) - 2, -1, -1):
            end = min(nums[i] + i, len(nums) - 1)
            for j in range(i + 1, end + 1):
                if made_it[j] is True:
                    made_it[i] = True
                    break

        return made_it[0]
