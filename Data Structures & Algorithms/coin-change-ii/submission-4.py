class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        N = len(coins)
        dp = [[0] *(amount+1) for i in range(N+1)]
        for i in range(N+1):
            dp[i][0] = 1
        for i in range(N-1,-1,-1):
            for j in range(amount+1):
                dp[i][j] = dp[i+1][j]
                if j -coins[i]>= 0:
                    dp[i][j] += dp[i][j-coins[i]]
        return dp[0][amount]



        # dp = {}
        # def dfs(i,sm):
        #     if sm == amount:
        #         return 1

        #     if i == N or sm > amount:
        #         return 0
        #     if (i,sm) in dp:
        #         return dp[(i,sm)]
        #     dp[(i,sm)] = dfs(i+1,sm) + dfs(i,sm+coins[i])
        #     return dp[(i,sm)]
        # return dfs(0,0)

        