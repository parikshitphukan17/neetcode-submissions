class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("infinity")] * (amount +1)
        dp[0] = 0
        for i in range(1,amount+1):
            for c in coins:
                if c <=i:
                    dp[i] = min(1+dp[i-c],dp[i])
        return dp[amount] if dp[amount] != float("infinity") else -1


        