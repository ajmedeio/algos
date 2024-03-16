def tokenize(p: str):
    tokens = []
    for c in p:
        if c == '*':
            tokens[-1] = (tokens[-1][0], True)
        else:
            tokens.append((c, False))
    return tokens    


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        t = tokenize(p)
        m, n = len(s), len(t)
        f = [[False] * (n+1) for _ in range(m+1)]
        f[0][0] = True
        for j in range(1, n+1):
            f[0][j] = f[0][j-1] if t[j-1][1] else False

        for i in range(1, m+1):
            for j in range(1, n+1):
                if (t[j-1][0] == s[i-1] or t[j-1][0] == ".") and t[j-1][1]:
                    f[i][j] = f[i-1][j] or f[i][j-1]
                elif (t[j-1][0] == s[i-1] or t[j-1][0] == "."):
                    f[i][j] = f[i-1][j-1]
                elif t[j-1][0] != s[i-1] and t[j-1][1]:
                    f[i][j] = f[i][j-1]

        return f[-1][-1]
