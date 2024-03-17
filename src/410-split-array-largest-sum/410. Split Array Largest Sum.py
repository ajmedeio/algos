class Solution:
    def splitArray(self, A: List[int], k: int) -> int:
        n = len(A)
        lo, hi = max(A), sum(A)
        while lo <= hi:
            i = lo + ((hi - lo) >> 1)
            n_parts, part_sum = 1, 0
            for j in range(n):
                part_sum += A[j]
                if part_sum > i:
                    n_parts += 1
                    part_sum = A[j]
            if n_parts > k:
                lo = i + 1
            else:
                hi = i - 1
        return lo