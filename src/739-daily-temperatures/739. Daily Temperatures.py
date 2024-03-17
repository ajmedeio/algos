class Solution:
    def dailyTemperatures(self, temps : List[int]) -> List[int]:
        n = len(temps)
        out = [0] * n
        s = []
        for i, t in enumerate(temps):
            while s and s[-1][0] < t:
                lesser = s.pop()
                out[lesser[1]] = i - lesser[1]
            s.append((t, i))
        return out
        