class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        q = x
        out = 0
        while q > 0:
            q, r = q // 10, q % 10
            out *= 10
            out += r
        return out == x