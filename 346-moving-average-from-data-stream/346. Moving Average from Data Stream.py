from collections import deque

class MovingAverage:

    def __init__(self, size: int):
        self.window = deque([]) # should use deqeue so we can popleft and pushright
        self.n = 0
        self.k = size
        self.sum = 0

    def next(self, val: int) -> float:
        if self.n < self.k:
            self.sum += val
            self.n += 1
            self.window.append(val)
            return self.sum / self.n
        else:  # n >= k
            left_val = self.window.popleft()
            self.window.append(val)
            self.sum -= left_val
            self.sum += val
            return self.sum / self.n


        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)