class Solution:
    def maximumUniqueSubarray(self, A: List[int]) -> int:
        n = len(A)
        s = 0
        c = Counter()
        m = 0
        l = 0
        for i in range(n):
            c[A[i]] += 1
            s += A[i]
            while len(c) < i-l+1:
                c[A[l]] -= 1
                s -= A[l]
                if c[A[l]] == 0:
                    del c[A[l]]
                l += 1
            m = max(m, s)
        return m
