class MinStack:

    def __init__(self):
        self.stack = []
        self.min_e = math.inf

    def push(self, val: int) -> None:
        self.min_e = min(self.min_e, val)
        self.stack.append((val, self.min_e))        

    def pop(self) -> None:
        top, min_e = self.stack.pop()
        self.min_e = self.stack[-1][1] if self.stack else math.inf
        return top

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()