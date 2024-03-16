m = {
    '2': ['a', 'b', 'c'],
    '3': ['d', 'e', 'f'],
    '4': ['g', 'h', 'i'],
    '5': ['j', 'k', 'l'],
    '6': ['m', 'n', 'o'],
    '7': ['p', 'q', 'r', 's'],
    '8': ['t', 'u', 'v'],
    '9': ['w', 'x', 'y', 'z'],
}

class Solution:
    def letterCombinations(self, s: str) -> List[str]:
        if len(s) == 0:
            return []
        out = []
        slate = []
        def rec(i):
            if i == len(s):
                out.append("".join(slate))
                return
            
            for c in m[s[i]]:
                slate.append(c)
                rec(i+1)
                slate.pop()
        
        rec(0)
        return out