from sortedcontainers import SortedList

class Solution:
    def medianSlidingWindow(self, A: List[int], k: int) -> List[float]:
        n = len(A)
        even = k % 2 == 0
        medians = []
        w = SortedList(A[0:k])
        median = (w[k//2 - 1] + w[k//2]) / 2 if even else w[k//2]
        medians.append(median)
        
        for i in range(k, n):
            w.remove(A[i-k])
            w.add(A[i])
            median = (w[k//2 - 1] + w[k//2]) / 2 if even else w[k//2]
            medians.append(median)
        return medians
