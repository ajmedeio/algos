class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        c = Counter()
        w = 0
        l = 0
        for i in range(n):
            c[s[i]] += 1
            while c[s[i]] > 1:
                c[s[l]] -= 1
                if c[s[l]] == 0:
                    del c[s[l]]
                l += 1
            w = max(w, i-l+1)
        return w
