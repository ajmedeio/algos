class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        n = len(s2)
        k = len(s1)
        c1 = Counter(s1)
        c2 = Counter(s2[0:k])
        if c1 == c2:
            return True
        for i in range(k, n):
            c2[s2[i-k]] -= 1
            c2[s2[i]] += 1
            if c1 == c2:
                return True
        return False