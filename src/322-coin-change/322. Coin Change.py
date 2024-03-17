from math import inf

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [inf for _ in range(amount + 1)]
        dp[0] = 0
        for i in range(1, amount + 1):
            n_coins = inf
            for d in coins:
                if i - d >= 0:
                    n_coins = min(n_coins, dp[i - d] + 1)
            dp[i] = n_coins
        return dp[amount] if dp[amount] != inf else -1
