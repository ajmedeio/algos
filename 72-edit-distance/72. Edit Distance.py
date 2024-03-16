class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # init 2D matrix word1 length n
        # and word2 length m
        n = len(word1)
        m = len(word2)
        f = [[0 for j in range(m + 1)] for i in range(n + 1)]

        # set f[0][j] for all j in 0 to m
        for j in range(m + 1):
            f[0][j] = j

        # set f[i][0] for all i in 0 to n
        for i in range(n + 1):
            f[i][0] = i

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                c = 0 if word1[i-1] == word2[j-1] else 1
                f[i][j] = min(f[i-1][j] + 1, f[i][j-1] + 1, f[i-1][j-1] + c)
        
        return f[-1][-1]