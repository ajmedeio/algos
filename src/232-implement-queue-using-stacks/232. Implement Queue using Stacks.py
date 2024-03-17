class MyQueue:

    def __init__(self):
        self.T = []
        self.S = []
        self.front = None

    def push(self, x: int) -> None:
        if len(self.T) == 0:
            self.front = x
        self.T.append(x)

    def pop(self) -> int:
        if len(self.S) == 0:
            while self.T:
                self.S.append(self.T.pop())
        return self.S.pop()

    def peek(self) -> int:
        if self.S:
            return self.S[-1]
        return self.front

    def empty(self) -> bool:
        return len(self.S) == 0 and len(self.T) == 0
