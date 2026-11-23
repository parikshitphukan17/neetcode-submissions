class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        N = len(prices)
        dp1 = [0]*2
        dp2 = [0]*2
        for i in range(N-1,-1,-1):
            cur = [0]*2
            for j in range(2):
                if j:
                    cur[j] = max(-prices[i]+dp1[0],dp1[j])
                else:
                    cur[j] = max(prices[i]+dp2[1],dp1[j])
            dp2 = dp1
            dp1 = cur
        return dp1[1]

        


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

        