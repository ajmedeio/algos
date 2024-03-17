class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        n = len(s)
        m = {}
        j = 0
        out = 0
        for i in range(len(s)):
            while j < n and (len(m) < 2 or s[j] in m):
                m[s[j]] = m.get(s[j], 0) + 1
                j += 1
            out = max(out, j-i)
            m[s[i]] -= 1
            if m[s[i]] == 0:
                del m[s[i]]
        return out