import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        ss = re.sub("[^a-z0-9]", "", s.lower())
        n = len(ss)
        i = 0
        j = n-1
        while i < j:
            if ss[i] != ss[j]:
                return False
            i += 1
            j -= 1
        return True