class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        m = {}
        vals = set()
        if len(s) != len(t):
            return False
        
        for i, l in enumerate(s):
            if l in m and m[l] != t[i]:
                return False
            if t[i] in vals:
                if l not in m:
                    return False
            else:
                vals.add(t[i])
                m[l] = t[i]
                
        return True