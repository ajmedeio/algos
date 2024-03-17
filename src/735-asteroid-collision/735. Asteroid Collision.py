def opposite(a, b):
    return a > 0 and b < 0 or a < 0 and b > 0

class Solution:
    def asteroidCollision(self, A: List[int]) -> List[int]:
        s = []
        for i, a in enumerate(A):
            if a > 0:
                s.append(a)
                continue
            while s and abs(s[-1]) < abs(a) and opposite(s[-1], a):
                s.pop()
            
            if s and abs(s[-1]) == abs(a) and opposite(s[-1], a): # equal and opposite, toss both
                s.pop()
            elif s and abs(s[-1]) > abs(a) and opposite(s[-1], a): # s[-1] > a
                pass  # do nothing as the current asteroid is clobbered by the one at top of stack
            else: # same sign, append
                s.append(a)
        return s
