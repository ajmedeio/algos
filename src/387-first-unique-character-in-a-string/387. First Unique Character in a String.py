class Solution:
    def firstUniqChar(self, s: str) -> int:
        n = len(s)
        c = Counter(s)
        for i in range(n):
            if c[s[i]] == 1:
                return i
        return -1