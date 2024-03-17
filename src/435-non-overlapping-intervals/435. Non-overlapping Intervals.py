class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key=lambda l: l[1])
        k = -math.inf
        out = 0
        for x, y in intervals:
            if x >= k:
                k = y
            else:
                out += 1
        return out