class Solution:
    def sumSubarrayMins(self, A: List[int]) -> int:
        MOD = (10 ** 9) + 7
        n = len(A)
        global_sum = 0
        sums = [0] * n
        s = []
        for i in range(n):
            local_sum = 0
            while s and s[-1][0] >= A[i]:
                s.pop()
            if s:
                span = i - s[-1][1]
                local_sum += sums[s[-1][1]]
            else:
                span = i + 1
            local_sum += span * A[i]
            sums[i] = local_sum
            global_sum = (global_sum + local_sum) % MOD
            s.append((A[i], i))
        return global_sum
