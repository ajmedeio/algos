class Solution:
    def minOperations(self, A: List[int]) -> int:
        n = len(A)
        B = sorted(set(A))
        out = n-1
        for i, l in enumerate(B):
            r = l + n - 1
            j = bisect_right(B, r)
            out = min(out, n - (j-i))
        return out
