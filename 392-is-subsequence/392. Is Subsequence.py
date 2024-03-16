class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False
        
        si = 0
        for ti, tl in enumerate(t):
            if si >= len(s):
                break
            sl = s[si]
            if sl == tl:
                si += 1
            
            
        return si == len(s)
        