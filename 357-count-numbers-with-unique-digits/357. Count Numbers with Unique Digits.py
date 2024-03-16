class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if 0 > n > 8:
            return 0
        if n == 0:
            return 1
        # we need to count the number of combinations we can make from 0 to 10 ^ n
        # 10^2 upto 99, two digits which is 10 + 9*9 
        # 10^3 upto 999, three digits, which is 10 + 9*9 + 9*9*8
        # 10^4 upto 9999, is four digits, which is 10 + 9*9 + 9*9*8 + 9*9*8*7
        all_terms = 10
        curr_term = 9

        for i in range(2, n+1):
            curr_term = (11 - i) * curr_term
            all_terms += curr_term

        return all_terms
