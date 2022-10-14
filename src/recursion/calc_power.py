
if __name__ == '__main__':
    def calculate_power(a, b):
        if b == 0:
            return 1
        else:
            t = calculate_power(a, b // 2)
            if b % 2 == 0:  # even
                return (t * t) % 1000000007
            else:  # odd
                return (a * t * t) % 1000000007

    #print(calculate_power(2, 10))

    def generate_all_subsets(S):
        out = []
        n = len(S)
        slate = []
        def rec(level):
            if level == n:
                out.append(''.join(slate))
                return
            rec(level + 1)
            slate.append(S[level])
            rec(level + 1)
            slate.pop()

        rec(0)
        return out
    print(generate_all_subsets('xy'))


