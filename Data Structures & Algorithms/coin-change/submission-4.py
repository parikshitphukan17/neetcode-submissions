class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        N = len(coins)
        dp = [float("infinity")]*(amount+1)
        dp[0] = 0
        for i in range(amount+1):
            for c in coins:
                if i-c>=0:
                    dp[i] = min(1 + dp[i-c],dp[i])
        return dp[amount] if dp[amount] != float("infinity") else -1






        # 12 = 1 +dp[2], 1+dp[7],1+dp[11]


        # dp[2] = 1 +dp[1]
        # dp[1] = 1 + dp[0]
        # dp[0] = 0




        