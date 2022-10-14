if __name__ == '__main__':
    def permute(S: str):
        out = []
        slate = ['' for _ in range(len(S))]

        def rec(S: str, i: int):
            if i == len(S):
                out.append(''.join(slate))
                return
            c = S[i]
            if c.isalpha():
                slate[i] = c.lower()
                rec(S, i + 1)
                slate[i] = c.upper()
                rec(S, i + 1)
            else:
                slate[i] = c
                rec(S, i + 1)

        rec(S, 0)
        return out

    for e in permute("a1b2"):
        print(e)
