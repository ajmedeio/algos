class Solution:
    def minWindow(self, s: str, t: str) -> str:
        c_w, c_t = Counter(), Counter(t)
        chars_captured = 0
        out = ""
        j = 0
        for i in range(len(s)):
            # increase window size and incorporate new characters
            while j < len(s) and chars_captured != len(c_t):
                if s[j] in c_t:
                    c_w[s[j]] += 1
                    if c_w[s[j]] == c_t[s[j]]:
                        chars_captured += 1
                j += 1
            # determine if we've found a new min
            if (out == "" or len(out) > (j-i)) and chars_captured == len(c_t):
                out = s[i:j]
            # get ready for next iteration by removing char
            if c_w[s[i]] > 0:
                c_w[s[i]] -= 1
                if c_w[s[i]] < c_t[s[i]]:
                    chars_captured -= 1
        return out
