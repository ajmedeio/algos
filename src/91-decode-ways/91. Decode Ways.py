class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0

        f = [0 for _ in range(n+1)]
        f[0] = 1 if 1 <= int(s[0]) <= 9 else 0
        f[1] = 0 if s[0] == '0' else 1
        for i in range(2, n+1):
            if s[i-1] != '0':
                f[i] = f[i-1]
            if 10 <= int(s[i-2:i]) <= 26:
                f[i] += f[i-2]
        
        return f[-1]
