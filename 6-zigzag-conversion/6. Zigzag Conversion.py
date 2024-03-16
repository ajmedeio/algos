class Solution:
    def convert(self, s: str, r: int) -> str:
        n = len(s)
        if r == 1:
            return s
        out = []
        top_gap = (r-1) * 2
        for r_i in range(r):
            i = r_i
            j = 0
            while i < n:
                out.append(s[i])
                if r_i == 0 or r_i == r-1:
                    i += top_gap
                elif j % 2 == 0:
                    i += (top_gap - (r_i * 2))
                else:
                    i += (r_i * 2)
                j += 1
        return "".join(out)
