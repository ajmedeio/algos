from collections import Counter

if __name__ == '__main__':
    def permutations(S: list[int]):
        out = []
        slate = [-1 for _ in range(len(S))]
        choices = Counter(S)
        n = len(S)

        def rec(choices, level, slate, out):
            if level == n:
                out.append(slate.copy())
                return
            for choice in choices:
                if choices[choice] > 0:
                    choices[choice] -= 1
                    slate[level] = choice
                    rec(choices, level + 1, slate, out)
                    choices[choice] += 1

        rec(choices, 0, slate, out)
        return out

    for e in permutations([1, 1, 2]):
        print(e)
