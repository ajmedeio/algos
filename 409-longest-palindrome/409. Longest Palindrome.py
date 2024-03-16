class Solution:
    def longestPalindrome(self, s: str) -> int:
        ls = Counter(list(s))
        length = 0
        for l in ls:
            k = l
            v = ls[k]
            if v % 2 == 0:
                length += v
            else:
                length += (v - 1)  
                
        return length if length == len(s) else length + 1