if __name__ == '__main__':
    def tower_of_hanoi(n):
        out = []
        def rec(n, src, dst, aux, out):
            if n == 1:
                # move src to dst
                out.append([src, dst])
                return out
            else:
                rec(n - 1, src, aux, dst, out)
                out.append([src, dst])
                return rec(n - 1, aux, dst, src, out)
        return rec(n, 1, 3, 2, out)

    for e in tower_of_hanoi(4):
        print(e)
