class Solution:
    def numOfSubarrays(self, A: List[int], k: int, threshold: int) -> int:
        n = len(A)
        w_sum = sum(A[0:k])
        averages = 1 if w_sum / k >= threshold else 0
        for i in range(k, n):
            w_sum -= A[i-k]
            w_sum += A[i]
            averages += 1 if w_sum / k >= threshold else 0
        return averages