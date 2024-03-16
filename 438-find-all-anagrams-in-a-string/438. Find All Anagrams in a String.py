class Solution:
    def findAnagrams(self, s: str, p: str) -> list[str]:
        out = []
        s_c = Counter(s[0:len(p)])
        p_c = Counter(p)
        if s_c == p_c:
            out.append(0)
        for i in range(len(s) - len(p)):
            s_c[s[i]] -= 1
            s_c[s[i + len(p)]] += 1
            out.append(i + 1) if s_c == p_c else None
        return out