class MyCircularQueue:

    def __init__(self, k: int):
        self.capacity = k
        self.Q = [0] * k
        self.head = 0
        self.tail = 0
        self.length = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.Q[self.tail] = value
        self.tail = (self.tail + 1) % self.capacity
        self.length += 1
        return True
        

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.head = (self.head + 1) % self.capacity
        self.length -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.Q[self.head]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.Q[self.tail - 1]

    def isEmpty(self) -> bool:
        return self.length == 0

    def isFull(self) -> bool:
        return self.length == self.capacity
        