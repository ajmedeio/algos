class Solution:
    def integerBreak(self, n: int) -> int:
        f = [0] * (n+1)
        f[1] = 1
        for i in range(2, n+1):
           for j in range(1, i):
               f[i] = max(f[i], max(j, f[j]) * max(i-j, f[i-j]))
        return f[n]