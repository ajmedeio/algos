from collections import deque


class Solution:
    def maxSlidingWindow(self, A: List[int], k: int) -> List[int]:
        n = len(A)
        out = []
        d = deque()
        for i in range(k):
            while d and d[-1][1] <= A[i]:
                d.pop()
            d.append((i, A[i]))
        out.append(d[0][1])
        
        for i in range(k, n):
            if d and d[0][0] == i - k:
                d.popleft()
            while d and d[-1][1] <= A[i]:
                d.pop()
            d.append((i, A[i]))
            out.append(d[0][1])
        return out
