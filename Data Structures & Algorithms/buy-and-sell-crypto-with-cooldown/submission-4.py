class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp ={}
        def dfs(i,buy):
            if i >= len(prices):
                return 0
            if (i,buy) in dp:
                return dp[(i,buy)]
            if buy:
                dp[(i,buy)] = max(-prices[i]+dfs(i+1,False),dfs(i+1,buy))
            else:
                dp[(i,buy)] = max(prices[i] +dfs(i+2,True),dfs(i+1,buy))
            return dp[(i,buy)]
        return dfs(0,True)

        