from heapq import heappop, heappush
import collections

class MaxStack:

    def __init__(self):
        self.S = []
        self.H = []
        self.removed = set()
        self.seq_id = 1

    def push(self, x: int) -> None:
        self.S.append((x, self.seq_id))
        heappush(self.H, (-x, -self.seq_id))
        self.seq_id += 1

    def pop(self) -> int:
        while self.S[-1][1] in self.removed:
            self.S.pop()
        e = self.S.pop()
        self.removed.add(e[1])
        return e[0]

    def top(self) -> int:
        while self.S[-1][1] in self.removed:
            self.S.pop()
        return self.S[-1][0]

    def peekMax(self) -> int:
        while -self.H[0][1] in self.removed:
            heappop(self.H)
        return -self.H[0][0]

    def popMax(self) -> int:
        while -self.H[0][1] in self.removed:
            heappop(self.H)
        e = heappop(self.H)
        self.removed.add(-e[1])
        return -e[0]
