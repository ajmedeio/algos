def is_palindrome(s) -> bool:
    n = len(s)
    i, j = 0, n-1
    while i < j:
        if s[i] == s[j]:
            i += 1
            j -= 1
        else:
            return False
    return True

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n, scratch, out = len(s), [], []
        def recurse(i):
            if i == n:
                out.append(scratch.copy())
                return
            for j in range(n-i):
                ss = s[i:i+j+1]
                if is_palindrome(ss):
                    scratch.append(ss)
                    recurse(i+j+1)
                    scratch.pop()
        recurse(0)
        return out
