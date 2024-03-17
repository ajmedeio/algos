from collections import Counter

class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        if k > len(s):
            return 0
        n = len(s)
        w = {}
        for i in range(0, k):
            if s[i] in w:
                w[s[i]] += 1
            else:
                w[s[i]] = 1
        count = 1 if len(w) == k else 0
        for i in range(k, n):
            w[s[i-k]] -= 1
            if w[s[i-k]] == 0:
                del w[s[i-k]]
            if s[i] in w:
                w[s[i]] += 1
            else:
                w[s[i]] = 1
            if len(w) == k:
                count += 1
            
        return count
