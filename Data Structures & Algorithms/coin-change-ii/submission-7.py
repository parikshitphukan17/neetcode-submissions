class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort()
        N = len(coins)
        dp =[[0] * (amount+1)for i in range(N+1)]
        for i in range(N+1):
            dp[i][amount] = 1
        for i in range(N-1,-1,-1):
            for j in range(amount,-1,-1):
                dp[i][j] = dp[i+1][j]
                if j+coins[i]<=amount:
                    dp[i][j] += dp[i][j+coins[i]]
        return dp[0][0]

        # def dfs(i,amt):
        #     if (i,amt) in dp:
        #         return dp[(i,amt)]
        #     if i == N or amt>amount:
        #         return 0
        #     if amt == amount:
        #         return 1
        #     dp[(i,amt)] = dfs(i,amt+coins[i]) + dfs(i+1,amt)
        #     return dp[(i,amt)]
        # return dfs(0,0)
        