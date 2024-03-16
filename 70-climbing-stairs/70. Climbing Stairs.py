class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1: return 1
        elif n < 1: return 0

        minus1 = 2
        minus2 = 1
        ways = 2
        for i in range(3, n+1):
            ways = minus1 + minus2
            minus2 = minus1
            minus1 = ways
        
        return ways
