class Solution:
    def isHappy(self, x: int) -> bool:
        def f(y):
            ans = 0
            while y != 0:
                ans += (y % 10) * (y % 10)
                y //= 10
            return ans
        tortoise, hare = x, x
        while True:
            tortoise = f(tortoise)
            hare = f(f(hare))
            if tortoise == hare: # cycle detected
                return tortoise == 1
