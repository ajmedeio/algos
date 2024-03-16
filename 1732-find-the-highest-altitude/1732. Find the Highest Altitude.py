class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        p = 0
        m = 0
        for g in gain:
            p += g
            m = max(m, p)
        return m