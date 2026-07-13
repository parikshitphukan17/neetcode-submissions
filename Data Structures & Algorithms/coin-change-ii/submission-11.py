class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        N = len(coins)
        dp = [[0] * (amount+1) for _ in range(N+1)]
        for i in range(N+1):
            dp[i][amount] = 1
        for i in range(N-1,-1,-1):
            for j in range(amount-1,-1,-1):
                dp[i][j] = dp[i+1][j]
                if j+coins[i]<= amount:
                    dp[i][j] += dp[i][j+coins[i]]
        return dp[0][0]
        
        # def dfs(i,cur):
        #     if cur == amount:
        #         return 1
        #     if i== len(coins) or cur>amount:
        #         return 0
        #     if (i,cur) in dp:
        #         return dp[(i,cur)]
        #     dp[(i,cur)] = dfs(i+1,cur) + dfs(i,cur+coins[i])
        #     return dp[(i,cur)]
        # return dfs(0,0)
        