class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        n = len(s)
        vowels = {'a', 'e', 'i', 'o', 'u'}
        w_sum = 0
        for i in range(0, k):
            if s[i] in vowels:
                w_sum += 1
        w_max = w_sum
        for i in range(k, n):
            w_sum -= 1 if s[i-k] in vowels else 0
            w_sum += 1 if s[i] in vowels else 0
            w_max = max(w_max, w_sum)
        return w_max
