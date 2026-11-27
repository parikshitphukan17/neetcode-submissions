class Solution: 
    def coinChange(self, coins: List[int], amount: int) -> int:
        N = len(coins)
        dp=[amount+1]*(amount+1)
        dp[0] = 0
        coins.sort()
        for i in range(amount+1):
            for c in coins:
                if c>i:
                    continue
                dp[i] = min(dp[i],1+dp[i-c])
        return dp[amount] if dp[amount]<=amount else -1 


     