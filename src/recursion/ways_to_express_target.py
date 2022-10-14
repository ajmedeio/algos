import re

if __name__ == '__main__':
    def compute_slate(slate: str):
        def partition_slate(slate: str) -> list[str]:
            out = [slate[0]]
            for i in range(1, len(slate)):
                if slate[i] in ['j', '*', '+']:
                    out.append(slate[i])
                    out.append('')
                else:
                    out[-1] += slate[i]
            return out
        out = partition_slate(slate)
        i = 0
        while i < len(out):
            if out[i] == 'j':
                out[i] = out[i - 1] + out[i + 1]
                out[i - 1] = out[i]
                del out[i:i+2]
                i -= 1
            else:
                i += 1
        i = 0
        while i < len(out):
            if out[i] == '*':
                out[i] = int(out[i - 1]) * int(out[i + 1])
                out[i - 1] = out[i]
                del out[i:i+2]
                i -= 1
            else:
                i += 1
        i = 0
        while i < len(out):
            if out[i] == '+':
                out[i] = int(out[i - 1]) + int(out[i + 1])
                out[i - 1] = out[i]
                del out[i:i+2]
                i -= 1
            else:
                i += 1
        return out[0]

    def express_target(s, t):
        out = set()

        def rec(s: str, t: int, i: int, slate: str, n: int):
            if i == n and compute_slate(slate) == t:
                out.add(slate.replace('j', ''))
                return
            elif i == n:
                return

            if i == 0:
                rec(s, t, i + 1, slate + s[i], n)
                rec(s, t, i + 1, slate + s[i], n)
                rec(s, t, i + 1, slate + s[i], n)
            else:
                rec(s, t, i + 1, slate + 'j' + s[i], n)
                rec(s, t, i + 1, slate + '*' + s[i], n)
                rec(s, t, i + 1, slate + '+' + s[i], n)

        rec(s, t, 0, '', len(s))
        return out

    for e in express_target('202', 4):
        print(e)
