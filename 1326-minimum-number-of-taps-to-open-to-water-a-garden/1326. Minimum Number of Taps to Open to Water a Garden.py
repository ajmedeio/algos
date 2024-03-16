class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        extents = [0] * (n+1)
        for i in range(n+1):
            r = ranges[i]
            s, e = max(0, i - r), min(n, i + r)
            extents[s] = max(extents[s], e)
        
        taps = 0
        reach = 0
        max_reach = 0

        for i in range(n+1):
            if i > max_reach:
                return -1
            
            if i > reach:
                taps += 1
                reach = max_reach
            max_reach = max(extents[i], max_reach)
        return taps
