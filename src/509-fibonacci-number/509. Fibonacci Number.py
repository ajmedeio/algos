class Solution:
    def fib(self, n: int) -> int:
        if n <= 1: return n
        
        prev = 1
        curr = 1
        for i in range(2, n):
            tempCurr = curr
            curr += prev
            prev = tempCurr
        
        return curr
