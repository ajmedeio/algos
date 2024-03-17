class MyStack:

    def __init__(self):
        self.q = deque()
        
    def push(self, x: int) -> None:
        self.q.append(x)

    def pop(self) -> int:
        n = len(self.q)
        while n > 1:
            self.q.append(self.q.popleft())
            n -= 1
        out = self.q.popleft()
        return out

    def top(self) -> int:
        n = len(self.q)
        while n > 1:
            self.q.append(self.q.popleft())
            n -= 1
        top = self.q.popleft()
        self.q.append(top)
        return top

    def empty(self) -> bool:
        return len(self.q) == 0
