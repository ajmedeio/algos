class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n = len(s1)
        m = len(s2)
        p = len(s3)
        if n + m != p:
            return False
        
        slate = ""
        @cache
        def rec(i, j):
            nonlocal slate
            if i == n and j == m:
                return slate == s3
            
            left, right = False, False
            if i < n and s3[i+j] == s1[i]:
                slate += s1[i]
                left = rec(i+1, j)
                slate = slate[:-1]
            if j < m and s3[i+j] == s2[j]:
                slate += s2[j]
                right = rec(i, j+1)
                slate = slate[:-1]
            return left or right

        return rec(0, 0)
