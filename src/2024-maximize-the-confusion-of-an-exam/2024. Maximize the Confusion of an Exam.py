class Solution:
    def maxConsecutiveAnswers(self, A: str, k: int) -> int:
        n = len(A)
        w_max = 0
        c = collections.Counter()

        for i in range(n):
            c[A[i]] += 1
            losing = min(c['T'], c['F'])

            if losing > k:
                # shrink window by one
                c[A[i-w_max]] -= 1
            else:
                w_max += 1
        return w_max

