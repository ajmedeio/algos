class Solution:
    def minimumAverageDifference(self, A: List[int]) -> int:
        t = sum(A)
        n = len(A)
        min_a_d, min_a_d_i = inf, 0
        p = 0
        for i in range(n):
            p += A[i]
            prefix_avg = p // (i+1)
            suffix_avg = (t-p) // (n-i-1) if i < n-1 else 0
            new_a_d = abs(prefix_avg - suffix_avg)
            if new_a_d < min_a_d:
                min_a_d = new_a_d
                min_a_d_i = i
        return min_a_d_i
