class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        n = len(words)
        out = []
        for i in range(n):
            w1 = words[i]
            for j in range(n):
                if i == j:
                    continue
                if w1 in words[j]:
                    out.append(w1)
                    break
        return out
