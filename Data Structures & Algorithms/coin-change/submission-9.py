class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("inf")] * (amount+1)
        dp[0] = 0
        for i in range(1,amount+1,1):
            for c in coins:
                if c>i:
                    continue
                dp[i] = min(dp[i],1+dp[i-c])
        return -1 if dp[amount] == float("inf") else dp[amount]


        # dp[1] = 1 + dp[0]
        # dp[2] = 1 +dp[1]
        # ・・
        # dp[12] min(1+dp[11],1+dp[7],1+dp[2])
        