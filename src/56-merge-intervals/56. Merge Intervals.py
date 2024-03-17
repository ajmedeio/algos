class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        meetings = sorted(intervals)
        prev_e = -math.inf
        out = []
        for s, e in meetings:
            if s <= prev_e:
                # merge prev with curr
                out[-1] = [min(out[-1][0], s), max(out[-1][1], e)]
            else:
                out.append([s, e])
            prev_e = max(out[-1][1], e)
        return out
