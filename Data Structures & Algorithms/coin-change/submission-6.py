class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount+1] *(amount+1)
        dp[0] = 0
        for i in range(1,amount+1):
            for j in coins:
                if j<=i:
                    dp[i] = min(dp[i],1+dp[i-j])
        return dp[amount] if dp[amount] != amount+1 else -1





        # 0 - 0
        # 1 -> 1 + dp[1-1]
        # 2 -> 1 + dp[2-1]
        # 3 -> 1 + dp[3-1] = 3 coins
        # 4 -> 1 + dp[4-1] = 4 coins
        # 5 -> min(1 + dp[5-1], 1 + dp[5-5])
        