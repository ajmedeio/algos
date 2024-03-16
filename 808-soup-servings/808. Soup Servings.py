class Solution:
    def soupServings(self, n: int) -> float:
        choices = [(100, 0), (75, 25), (50, 50), (25, 75)]
        if n >= 5000:
            return 1.0
        @cache
        def rec(a, b):
            if a <= 0 and b <= 0:
                return 0.5
            if a <= 0:
                return 1
            if b <= 0:
                return 0

            p = 0
            for da, db in choices:
                p += rec(a - da, b - db)
            return 0.25 * p
        return rec(n, n)
    
    def soupServingsIter(self, n: int) -> float:
        n = math.ceil(n / 25)
        choices = [(4, 0), (3, 1), (2, 2), (1, 3)]
        f = [[0] * n for _ in range(n)]
        
        # base cases
        f[0][0] = 0.5
        for j in range(1, n):
            f[0][j] = 1
        
        for i in range(1, n):
            for j in range(1, n):
                p = 0
                for da, db in choices:
                    if i - da >= 0 and j - db >= 0:
                        p += f[i - da][j - db]
                f[i][j] = .25 * p
        return sum(f)
