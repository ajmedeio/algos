if __name__ == '__main__':
    def additive_sequence_iter(n, b1, b2):
        while True:
            if n == 1:
                return b2
            else:
                n, b1, b2 = n - 1, b2, b1 + b2

    def find_fibonacci(n: int):
        return additive_sequence_iter(n, 0, 1)

    print(find_fibonacci(6))
