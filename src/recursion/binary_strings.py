if __name__ == '__main__':
    def get_binary_strings(n: int):
        out = []
        scratch = ['' for _ in range(n)]
        def rec(level):
            if level == n:
                out.append(''.join(scratch))
            else:
                scratch[level] = '0'
                rec(level + 1)
                scratch[level] = '1'
                rec(level + 1)
        rec(0)
        return out


    for e in get_binary_strings(3):
        print(e)


    def binary_strings_iter(n):
        result = ['0', '1']
        for i in range(2, n + 1):
            new_result = []
            for s in result:
                new_result.append(s + '0')
                new_result.append(s + '1')
            result = new_result
        return result
    # for e in binary_strings(3):
    #    print(e)
