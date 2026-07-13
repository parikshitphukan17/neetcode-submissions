class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        dp = [float("inf")]*(amount+1)
        dp[0] = 0
        for i in range(1,amount+1):
            for c in coins:
                if c<=i:
                    dp[i] = min(dp[i],1+dp[i-c])
        return dp[amount] if dp[amount]!= float("inf") else -1
                





        # 0-0
        # 1-1
        # 2-1+dp[1]
        # 3-1+dp[2]
        # 4-1+dp[3]
        # 5-1+dp[0]
        # 6-1+dp[1],1+dp[5]
        # 7-

        