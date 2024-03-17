class NumMatrix:

    def __init__(self, M: List[List[int]]):
        self.n = len(M)
        self.m = len(M[0])
        P = [[0] * self.m for _ in range(self.n)]
        def get(M, i, j):
            if 0 <= i < self.n and 0 <= j < self.m:
                return M[i][j]
            else:
                return 0

        for i in range(self.n):
            for j in range(self.m):
                P[i][j] = (
                    get(M, i, j)
                    + get(P, i-1, j)
                    + get(P, i, j-1)
                    - get(P, i-1, j-1)
                )
        self.P = P

    def sumRegion(self, r1: int, c1: int, r2: int, c2: int) -> int:
        def get(P, i, j):
            if 0 <= i < self.n and 0 <= j < self.m:
                return P[i][j]
            else:
                return 0
        return (
            get(self.P, r2, c2)
            - get(self.P, r2, c1-1)
            - get(self.P, r1-1, c2)
            + get(self.P, r1-1, c1-1)
        )
