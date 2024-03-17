class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        f = [0 for _ in range(days[-1] + 1)]
        days = set(days)
        for i in range(1, len(f)):
            if i in days:
                f1 = f[max(i-1, 0)]
                f7 = f[max(i-7, 0)]
                f30 = f[max(i-30, 0)]
                f[i] = min(f1 + costs[0], f7 + costs[1], f30 + costs[2])
            else:
                f[i] = f[i-1]
        return f[-1]
