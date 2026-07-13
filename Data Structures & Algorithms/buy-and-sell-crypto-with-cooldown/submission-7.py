class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        N = len(prices)
        dp = [[0]*(2) for i in range(N+2)]
        for i in range(N-1,-1,-1):
            for buy in [True,False]:
                if buy:
                    dp[i][buy] = max(-prices[i]+dp[i+1][False],dp[i+1][buy])
                else:
                    dp[i][buy] = max(prices[i]+dp[i+2][True],dp[i+1][buy])
        return dp[0][True]

        # def dfs(buy,i):
        #     if i>=N:
        #         return 0
        #     if (buy,i) in dp:
        #         return dp[(buy,i)]
        #     if buy:
        #         dp[(buy,i)] = max(-prices[i]+dfs(False,i+1),dfs(buy,i+1))
        #     else:
        #         dp[(buy,i)] = max(prices[i]+dfs(True,i+2),dfs(buy,i+1))
        #     return dp[(buy,i)]
        # return dfs(True,0)



        