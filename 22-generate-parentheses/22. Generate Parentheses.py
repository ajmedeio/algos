class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        out, stack = [], []
        def recurse(n_l, n_r):
            if n_l == n_r == n:
                out.append("".join(stack))
                return
            if n_l < n:
                stack.append("(")
                recurse(n_l + 1, n_r)
                stack.pop()
            if n_l > n_r:
                stack.append(")")
                recurse(n_l, n_r + 1)
                stack.pop()
        recurse(0, 0)
        return out