class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(" ", "")
        n = len(s)
        S = []
        ans, operand, sign = 0, 0, 1
        for c in s:
            if c.isdigit():
                operand = (operand * 10) + int(c)
            elif c == "+":
                ans += sign * operand
                sign = 1
                operand = 0
            elif c == "-":
                ans += sign * operand
                sign = -1
                operand = 0
            elif c == "(":
                S.append(ans)
                S.append(sign)
                ans = 0
                sign = 1
                operand = 0
            elif c == ")":
                ans += sign * operand
                ans *= S.pop()
                ans += S.pop()
                operand = 0
                sign = 1
        return ans + (sign * operand)
