class Solution:
    def mergeAlternately(self, A: str, B: str) -> str:
        i, j, n, m = 0, 0, len(A), len(B)
        out = []
        while i < n and j < m:
            out.append(A[i])
            out.append(B[j])
            i += 1
            j += 1
        while i < n:
            out.append(A[i])
            i += 1
        while j < m:
            out.append(B[j])
            j += 1
        return "".join(out)