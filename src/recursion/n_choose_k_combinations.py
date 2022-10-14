if __name__ == '__main__':

    def cycle(start, stop, num_cycles: int=1):
        pass

    def find_combinations(n, k):
        out = []
        slate = []
        def rec(level):
            if len(slate) == k:
                out.append(slate.copy())
                return
            for i in range(level, n + 1):
                slate.append(i)
                rec(i+1)
                slate.pop()

        rec(1)
        return out

    for e in find_combinations(5, 2):
        print(e)
