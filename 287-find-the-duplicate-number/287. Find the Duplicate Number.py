class Solution:
    def findDuplicate(self, A: List[int]) -> int:
        n = len(A)
        def f(x):
            return A[x]
        cap_1, cap_2, t, h = 0, 0, 0, 0
        while cap_1 < n:
            cap_1 += 1
            t = f(t)
            h = f(f(h))
            if t == h:
                break
        
        t2 = 0
        while t2 != t and cap_2 < n:
            cap_2 += 1
            t = f(t)
            t2 = f(t2)
        return t
