class Solution:
    def dietPlanPerformance(self, A: List[int], k: int, lo: int, hi: int) -> int:
        n = len(A)
        T = sum(A[0:k])
        if T > hi:
            points = +1
        elif T < lo:
            points = -1
        else:
            points = 0

        for i in range(k, n):
            T += A[i] - A[i-k]
            if T > hi:
                points += 1
            elif T < lo:
                points -= 1
        return points
