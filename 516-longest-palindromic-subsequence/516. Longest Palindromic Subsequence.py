class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        memo = {}
        def rec(i, j):
            if (i, j) in memo:  # check cache
                return memo[(i, j)]

            if j <= i:  # base case
                memo[(i, j)] = 1 if i == j else 0
                return memo[(i, j)]
            
            if s[i] == s[j]:
                ans = rec(i+1, j-1) + 2
            else:
                ans = max(rec(i+1, j), rec(i, j-1))
            
            memo[(i, j)] = ans
            return ans
        
        return rec(0, len(s)-1)