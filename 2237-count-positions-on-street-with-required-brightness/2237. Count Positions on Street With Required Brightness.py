class Solution:
    def meetRequirement(self, n: int, L: List[List[int]], R: List[int]) -> int:
        out = 0
        I = [0] * n
        for p, r in L:
            I[max(0, p - r)] += 1
            if p+r+1 < n:
                I[p+r+1] -= 1
        for i in range(1, n):
            I[i] += I[i-1]
        for i in range(n):
            if I[i] >= R[i]:
                out += 1
        return out
