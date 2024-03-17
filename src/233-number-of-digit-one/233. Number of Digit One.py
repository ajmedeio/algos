class Solution:
    def countDigitOne(self, n: int) -> int:
        c = 0
        for i in range(n + 1):
            n_str = str(i)
            for ch in n_str:
                if ch == '1':
                    c += 1
        return c

    def countDigitOneBlaasdas(self, n: int) -> int:
        print('no')
        c = 0
        order = 0
        test_n = n
        while test_n // 10 ** (order) > 0:
            order += 1
        print(order)
        for i in range(1, order + 1):
            divisor = 10 ** i
            place = 10 ** (i - 1)
            if n >= divisor:
                dividend = math.ceil(n / divisor)
                print(dividend)
                c += dividend * place
            elif n < divisor:
                remainder = n % divisor
                c += remainder + 1
        return c
