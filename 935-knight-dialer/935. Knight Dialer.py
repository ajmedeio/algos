CHOICES = {
    0: [4, 6],
    1: [6, 8],
    2: [7, 9],
    3: [4, 8],
    4: [0, 3, 9],
    5: [],
    6: [0, 1, 7],
    7: [2, 6],
    8: [1, 3],
    9: [2, 4],
}

class Solution:
    def knightDialer(self, n: int) -> int:
        modulo = (10**9) + 7
        f = [[0 for _ in range(10)] for _ in range(n + 1)]
        for row in range(2):
            for col in range(10):
                f[row][col] = 1

        for row in range(2, n+1):
            for col in range(0, 10):
                for choice in CHOICES[col]:
                    f[row][col] += f[row-1][choice]

        return sum(f[-1]) % modulo
