if __name__ == '__main__':
    def generate_all_subsets_of_a_set(S: str):
        out = []
        slate = ['' for _ in range(len(S))]

        def rec(i):
            if i == len(S):
                out.append(list(filter(lambda e: e != '', slate)))
            else:
                slate[i] = ''
                rec(i + 1)
                slate[i] = S[i]
                rec(i + 1)
        rec(0)
        return out

    for e in generate_all_subsets_of_a_set('xy'):
        print(e)
