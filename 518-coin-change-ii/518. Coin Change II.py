class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}
        c = coins  # alias for shorter variable name
        n = len(coins)
        def f(i, t):
            if (i, t) in memo:
                return memo[(i, t)]
            if t == 0:
                return 1
            if t < 0:
                return 0
            if i < 0: 
                return 0

            result = f(i-1, t) + f(i, t - c[i])
            memo[(i, t)] = result
            return result

        return f(n-1, amount)
            