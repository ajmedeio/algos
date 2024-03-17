class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        mrc = 0
        counts = Counter()
        l = 0
        out = 0
        for r in range(len(s)):
            cr = s[r]
            counts[cr] += 1
            mrc = max(counts[cr], mrc)
            
            if (r - l + 1) - mrc > k:
                cl = s[l]
                counts[cl] -= 1
                l += 1
            
            out = max(out, r - l + 1)
                        
        return out
