class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        memo = {}
        def rec(s, i, j) -> List[int]:
            if (i, j) in memo:
                return memo[(i, j)]
            if s[i:j].isdigit():
                return [int(s[i:j])]
            
            out = []
            for k in range(i, j):
                if not s[k].isdigit():
                    l_r = rec(s, i, k)
                    r_r = rec(s, k+1, j)
                    for l in l_r:
                        for r in r_r:
                            if s[k] == '+':
                                out.append(l + r)
                            elif s[k] == '-':
                                out.append(l - r)
                            else: # '*'
                                out.append(l * r)
            memo[(i, j)] = out
            return out
        
        return rec(expression, 0, len(expression))