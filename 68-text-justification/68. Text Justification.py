class Solution:
    def fullJustify(self, A: List[str], max_w: int) -> List[str]:
        n = len(A)
        lines = []
        line = A[0]
        for i in range(1, n):
            if len(line) + 1 + len(A[i]) > max_w:
                lines.append(line)
                line = A[i]
            else:
                line += " " + A[i]
        lines.append(line)
        
        m = len(lines)
        for i in range(0, m-1):
            # distribute empty space evenly, count the number of words
            n_gaps = lines[i].count(" ")
            if n_gaps == 0:
                lines[i] = lines[i] + (" " * (max_w - len(lines[i])))
            else:
                n_extra_spaces = max_w - len(lines[i])
                q, r = n_extra_spaces // n_gaps, n_extra_spaces % n_gaps
                lines[i] = lines[i].replace(" ", " " * (q+1))
                lines[i] = lines[i].replace(" " * (q+1), " " * (q+2), r)

        lines[-1] = lines[-1] + (" " * (max_w - len(lines[-1])))
        return lines