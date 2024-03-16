def operate(operator, left, right):
    l = int(left)
    r = int(right)
    if operator == "+":
        return l + r
    elif operator == "-":
        return l - r
    elif operator == "*":
        return l * r
    elif operator == "/":
        return int(l / r)

def isnumerictoken(t):
    try:
        v = int(t)
        return True
    except ValueError:
        return False

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if isnumerictoken(t):
                stack.append(t)
            else:
                dr = stack.pop()
                dl = stack.pop()
                dn = operate(t, dl, dr)
                stack.append(dn)
        return int(stack[-1])
