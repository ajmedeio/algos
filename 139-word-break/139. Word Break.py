class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        D = set(wordDict)
        n = len(s)

        @cache
        def f(ss):
            if len(ss) == 0:
                return True
            out = False
            for i in range(0, len(ss)):
                out |= ss[:i+1] in D and f(ss[i+1:])
            return out
        return f(s)
