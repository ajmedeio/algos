if __name__ == '__main__':
    def is_palindrome(s, l, r):
        if len(s) == 0:
            return False
        while l <= r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True


    def can_prune():
        return False

    def generate_palindromic_decompositions(s):
        out = []
        n = len(s)
        def rec(candidate, i):
            if i == n:
                out.append(candidate)
                return

            for j in range(i, len(s)):
                if is_palindrome(s, i, j):
                    # now we can either add the current char to the palindrome
                    # or we can not add the current char
                    if len(candidate) <= 0:
                        rec(s[i:(j - i + 1)], i + 1)
                    else:
                        rec(candidate + '|' + s[i:(j - i + 1)], i + 1)

        rec('', 0)
        return out


    for e in generate_palindromic_decompositions('abracadabra'):
        print(e)
