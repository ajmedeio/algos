class NumArray:

    def __init__(self, A: List[int]):
        n = len(A)
        self.P = [0] * (n+1)
        s = 0
        for i in range(n):
            s += A[i]
            self.P[i+1] = s

    def sumRange(self, i: int, j: int) -> int:
        return self.P[j+1] - self.P[i]
        