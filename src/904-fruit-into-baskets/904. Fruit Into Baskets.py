class Solution:
    def totalFruit(self, A: list[int]) -> int:
        n = len(A)
        c = Counter()
        l = 0
        w = 0
        for i in range(n):
            c[A[i]] += 1
            while l <= i and len(c) > 2:
                c[A[l]] -= 1
                if c[A[l]] == 0:
                    del c[A[l]]
                l += 1
            w = max(w, i-l+1)
        return w
