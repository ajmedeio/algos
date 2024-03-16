class Solution:
    def findMaxAverage(self, A: List[int], k: int) -> float:
        n = len(A)
        w_sum = sum(A[0:k])
        avg_max = w_sum / k
        for i in range(k, n):
            w_sum -= A[i-k]
            w_sum += A[i]
            avg_max = max(avg_max, w_sum / k)
        return avg_max