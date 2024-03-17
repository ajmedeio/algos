from heapq import heapify, heappush, heappop

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.h = []
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        if len(self.h) < self.k:
            heappush(self.h, val)
        elif self.h[0] < val:
            heappop(self.h)
            heappush(self.h, val)
        return self.h[0]
