class Solution:
    def numTilings(self, n: int) -> int:
        MOD = 10**9 + 7
        if n <= 2:
            return n

        f = [0 for _ in range(n+1)]
        l = [0 for _ in range(n+1)]

        f[1] = 1
        f[2] = 2
        l[2] = 1

        for i in range(3, n+1):
            f[i] = (f[i-1] + f[i-2] + 2*l[i-1]) % MOD
            l[i] = (l[i-1] + f[i-2]) % MOD

        return f[n]