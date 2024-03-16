class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        n = len(s)
        w = 0
        c = Counter()
        l = 0
        for i in range(n):
            c[s[i]] += 1
            while len(c) > k:
                c[s[l]] -= 1
                if c[s[l]] == 0:
                    del c[s[l]]
                l += 1
            w = max(w, i-l+1)
        return w
