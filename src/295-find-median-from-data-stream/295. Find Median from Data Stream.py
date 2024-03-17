from heapq import heapify, heappush, heappop
from math import inf

class MedianFinder:

    def __init__(self):
        self.H_l = []
        self.H_r = []
        self.n = 0

    def addNum(self, v: int) -> None:
        heappush(self.H_l, -v)
        heappush(self.H_r, -heappop(self.H_l))

        if len(self.H_l) < len(self.H_r):
            heappush(self.H_l, -heappop(self.H_r))

    def findMedian(self) -> float:
        if len(self.H_l) > len(self.H_r):
            return -self.H_l[0]
        else:
            return (-self.H_l[0] + self.H_r[0]) / 2
