class Solution:
        def findTheLongestSubstring(self, s: str) -> int:
            c = {0: 0}
            bit_pos = {'a': 0,'e': 1,'i': 2,'o': 3,'u': 4}
            p = 0
            out = 0
            for i, ch in enumerate(s):
                if ch in bit_pos:
                    p ^= 1 << bit_pos[ch]

                if p in c:
                    out = max(out, i+1 - c[p])
                else:
                    c[p] = i+1
            return out
