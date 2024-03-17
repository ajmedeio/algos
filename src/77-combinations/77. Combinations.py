class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        slate = []
        out = []
        def rec(level, i):
            if level == k:
                out.append(slate[:])
                return
            for j in range(i, n+1):
                slate.append(j)
                rec(level + 1, j + 1)
                del slate[-1]
        
        rec(0, 1)
        return out
