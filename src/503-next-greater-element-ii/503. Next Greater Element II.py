class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ns = nums + nums
        s = []
        out = [-1] * (2 * n)
        for i, e in enumerate(ns):
            while s and s[-1][0] < e:
                top = s.pop()
                out[top[1]] = e
            s.append((e, i))
        return out[:n]
