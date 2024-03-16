class Solution:
    def garbageCollection(self, G: List[str], T: List[int]) -> int:
        s = set()
        out = 0
        n = len(T)
        for i in range(n-1, -1, -1):
            if len(s) < 3:
                for c in G[i+1]:
                    s.add(c)
            out += len(s) * T[i] + len(G[i+1])
        out += len(G[0])
        return out
