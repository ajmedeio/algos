class Solution:
    def shipWithinDays(self, W: List[int], d: int) -> int:
        n = len(W)
        lo, hi = max(W), sum(W)
        while lo <= hi:
            c = lo + ((hi - lo) >> 1)
            trip_c = 0
            n_trips = 1
            for i in range(n):
                trip_c += W[i]
                if trip_c > c:
                    n_trips += 1
                    trip_c = W[i]
            if n_trips <= d:
                hi = c - 1
            elif n_trips > d:
                lo = c + 1
        return lo