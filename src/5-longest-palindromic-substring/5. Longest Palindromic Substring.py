def expand_while_palindrome(s, i, j):
    while 0 <= i <= j < len(s) and s[i] == s[j]:
        i -= 1
        j += 1
    return j - i - 1, i+1, j

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n, out = len(s), (-inf, 0, 0)
        for i in range(n):
            out = max(out, expand_while_palindrome(s, i, i))
        for i in range(n-1):
            out = max(out, expand_while_palindrome(s, i, i+1))
        return s[out[1]:out[2]]
