class Solution:
    def corpFlightBookings(self, B: List[List[int]], n: int) -> List[int]:
        out = [0] * n
        for i, j, seats in B:
            out[i-1] += seats
            if j < n:
                out[j] -= seats

        for i in range(1, n):
            out[i] += out[i-1]
        return out