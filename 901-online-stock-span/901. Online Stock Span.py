class StockSpanner:

    def __init__(self):
        self.s = []

    def next(self, price: int) -> int:
        # what if s is empty?
        i = 1
        while self.s and price >= self.s[-1][0]:
            i += self.s.pop()[1]
        self.s.append((price, i))
        return i
