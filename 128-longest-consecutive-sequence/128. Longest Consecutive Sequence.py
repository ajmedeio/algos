class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)

        max_streak = 0
        for n in s:
            if n - 1 not in s:
                streak = 0
                c = n
                while c in s:
                    streak += 1
                    c += 1
                max_streak = max(max_streak, streak)
        return max_streak
