class Solution:
    def circularArrayLoop(self, A: List[int]) -> bool:
        n = len(A)
        def f(x):
            return (x + A[x]) % n

        for i in range(n):
            if A[i] == 0:
                continue

            tortoise, hare = i, i
            while True:
                tortoise = f(tortoise)
                hare = f(f(hare))
                if tortoise == hare: # cycle detected
                    # now determine sign of path and cycle_length
                    sign = +1 if A[hare] > 0 else -1
                    tortoise2 = f(tortoise)
                    cycle_length = 1
                    same_sign = True
                    while tortoise2 != tortoise:
                        sign2 = +1 if A[tortoise2] > 0 else -1
                        same_sign &= sign2 == sign
                        cycle_length += 1
                        tortoise2 = f(tortoise2)
                    if cycle_length > 1 and same_sign:
                        return True
                    else:
                        tortoise2 = i
                        while A[tortoise2] != 0:
                            tmp = f(tortoise2)
                            A[tortoise2] = 0
                            tortoise2 = tmp
                        break
        return False