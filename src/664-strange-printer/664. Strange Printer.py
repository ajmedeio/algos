class Solution:
    def strangePrinter(self, s: str) -> int:
        n = len(s)
        f = [[n] * n for _ in range(n)]

        for length in range(1, n + 1):
            for left in range(n - length + 1):
                right = left + length - 1
                j = -1
                for i in range(left, right):
                    if s[i] != s[right] and j == -1:
                        j = i
                    if j != -1:
                        f[left][right] = min(f[left][right], 1 + f[j][i] + f[i + 1][right])
        
                if j == -1:
                    f[left][right] = 0

        return f[0][n - 1] + 1