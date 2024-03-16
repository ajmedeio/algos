class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        ranges.sort(key=lambda t: t[0])
        l, r = left, right
        for s, e in ranges:
            l = e+1 if s <= l <= e else l
            r = s if s <= r <= e else r
        return r < l
