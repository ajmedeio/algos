class Solution:
    def numIdenticalPairs(self, A: List[int]) -> int:
        C = Counter()
        out = 0
        for x in A:
            out += C[x]
            C[x] += 1
        return out
