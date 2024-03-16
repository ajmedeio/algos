class Solution:
    def canCross(self, S: List[int]) -> bool:
        n = len(S)
        m = {}
        m = {s: i for i, s in enumerate(S)}
        
        f = [[False] * (n+1) for _ in range(n)]
        f[0][0] = True
        for i in range(0, n):
            for j in range(0, n+1):
                if f[i][j] == True:
                    if S[i] + j in m:
                        f[m[S[i] + j]][j] = True
                    
                    if S[i] + j + 1 in m:
                        f[m[S[i] + j + 1]][j + 1] = True

                    if S[i] + j - 1 in m:
                        f[m[S[i] + j - 1]][j - 1] = True
        
        return any(f[n-1][:])
