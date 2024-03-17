class Solution:
    def longestOnes(self, A: List[int], k: int) -> int:
        n = len(A)
        flips = k
        w = 0
        l = 0
        for i in range(n):
            if A[i] == 0:
                flips -= 1
            while l <= i and flips < 0:
                if A[l] == 0:
                    flips += 1
                l += 1
            w = max(w, i - l + 1)
        return w
