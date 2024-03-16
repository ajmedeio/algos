def remove_dup_stars(p: str):
    t = ""
    prev = None
    for c in p:
        if prev == "*" and c == "*":
            continue
        t += c
        prev = c
    return t

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        p = remove_dup_stars(p)
        m, n = len(p), len(s)
        f = [[False] * (n+1) for _ in range(m+1)]
        f[0][0] = True
        for i in range(1, m+1):
            if p[i-1] == "*":
                f[i][0] = f[i-1][0]
            else:
                f[i][0] = False
        for j in range(1, n+1):
            f[0][j] = False

        for i in range(1, m+1):
            for j in range(1, n+1):
                if p[i-1] == '*':
                    f[i][j] = f[i-1][j] or f[i][j-1]
                elif p[i-1] == s[j-1] or p[i-1] == '?':
                    f[i][j] = f[i-1][j-1]
                else:
                    f[i][j] = False

        return f[-1][-1]
