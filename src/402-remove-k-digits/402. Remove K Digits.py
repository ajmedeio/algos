class Solution:
    def removeKdigits(self, A: str, k: int) -> str:
        n, s = len(A), deque()
        if k == n:
            return "0"
        for i in range(n):
            while k > 0 and s and s[-1] > A[i]:
                s.pop()
                k -= 1
            s.append(A[i])

        while k > 0:
            s.pop()
            k -= 1
        while s and s[0] == "0":
            s.popleft()
        return "".join(s) if len(s) > 0 else "0"
