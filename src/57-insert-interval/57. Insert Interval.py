class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        out = []
        bisect.insort(intervals, newInterval)
        for s, e in intervals:
            if out and s <= out[-1][1]:  # merge
                out[-1][1] = max(e, out[-1][1])
            else:  # append
                out.append([s, e])
        return out
