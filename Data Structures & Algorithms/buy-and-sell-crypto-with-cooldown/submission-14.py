class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # dp = [[0]*2 for _ in range(len(prices)+2)]
        # for i in range(len(prices)-1,-1,-1):
        #     for buy in [True,False]:
        #         if buy:
        #             dp[i][buy] = max(-prices[i]+dp[i+1][False], dp[i+1][buy])
        #         else:
        #             dp[i][buy] = max(prices[i]+dp[i+2][True], dp[i+1][buy])
        # return dp[0][True]

        N = len(prices)
        dp = [[0,0] for _ in range(N+2)]

        for i in range(N-1,-1,-1):
            for buy in [0,1]:
                if buy:
                    dp[i][buy] = max(-prices[i]+dp[i+1][0],dp[i+1][buy])
                else:
                    dp[i][buy] = max(prices[i]+dp[i+2][1],dp[i+1][buy])
        return dp[0][1]


        # dp = {}
        # def dfs(i,buy):
        #     if i>=N:
        #         return 0

        #     if (i,buy) in dp:
        #         return dp[(i,buy)]
        #     if buy:
        #         dp[(i,buy)] = max(-prices[i]+dfs(i+1,False),dfs(i+1,buy))
        #     else:
        #         dp[(i,buy)] = max(prices[i]+dfs(i+2,True),dfs(i+1,buy))
        #     return dp[(i,buy)]
        # return dfs(0,True)


            

            

        