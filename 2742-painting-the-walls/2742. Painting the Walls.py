class Solution:
    def paintWalls(self, C: List[int], T: List[int]) -> int:
        n = len(C)
        knockout = [False] * n
        def rec(x, accumulated_time, accumulated_cost):
            if accumulated_time + x >= n:
                return accumulated_cost
            m = inf
            for j in range(n):
                if knockout[j] is False:
                    knockout[j] = True
                    m = min(m, rec(x + 1, accumulated_time + T[j], accumulated_cost + C[j]))
                    knockout[j] = False
            return m
        return rec(0, 0, 0)
