class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        n = len(str1)
        m = len(str2)

        # arranged where str1 is across the rows
        f = [[0 for _ in range(m+1)] for _ in range(n+1)]

        for i in range(n+1):
            f[i][0] = 0

        for j in range(m+1):
            f[0][j] = 0

        for i in range(1, n+1):
            for j in range(1, m+1):
                if str1[i-1] == str2[j-1]:
                    s = 1
                else:
                    s = 0
                # maximize matches for find LCS (longest common subsequence) alignment
                f[i][j] = max(f[i-1][j], f[i][j-1], f[i-1][j-1] + s)
        
        i = n
        j = m
        out = []
        while i != 0 and j != 0:  # if we hit the edge, stop and append the rest of the letter from either 1 or 2
            # trace back through table
            if f[i][j] == f[i-1][j]:
                out.append(str1[i-1])
                i -= 1
            elif f[i][j] == f[i][j-1]:
                out.append(str2[j-1])
                j -= 1
            else:  # match
                out.append(str1[i-1])
                i, j = i-1, j-1
            
        while i != 0:
            out.append(str1[i-1])
            i -= 1
        
        while j != 0:
            out.append(str2[j-1])
            j -= 1
        
        out.reverse()
        return out