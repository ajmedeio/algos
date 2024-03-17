class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        stk = []
        m = {
            "(": ")",
            "[": "]",
            "{": "}",
        }
        for i in range(len(s)):
            if s[i] in m:
                stk.append(s[i])
            else:
                if len(stk) == 0:
                    return False

                top = stk.pop()
                if m[top] != s[i]:
                    return False
        return len(stk) == 0