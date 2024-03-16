class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        n, dictionary_set = len(s), set(dictionary)
        @cache
        def f(i):
            if i == n:
                return 0
            # To count this character as a left over character 
            # move to index 'start + 1'
            out = f(i + 1) + 1
            for j in range(i, n):
                curr = s[i:j+1]
                if curr in dictionary_set:
                    out = min(out, f(j + 1))
            return out

        return f(0)
