if __name__ == '__main__':
    def permute_array(S: list[int]):
        out = []
        slate = [-1 for _ in range(len(S))]
        knockout = [0 for _ in range(len(S))]
        n = len(S)

        def rec(level: int):
            if level == n:
                out.append(slate.copy())
                return
            for i, c in enumerate(S):
                if knockout[i] == 0:
                    knockout[i] = 1
                    slate[level] = c
                    rec(level + 1)
                    knockout[i] = 0

        rec(0)
        return out

    for e in permute_array([1, 2, 3]):
        print(e)
