class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        def dfs(i,buy):
            if i >= len(prices):
                return 0
            if buy:
                return max(-prices[i]+dfs(i+1,False),dfs(i+1,buy))
            else:
                return max(prices[i] +dfs(i+2,True),dfs(i+1,buy))
        return dfs(0,True)

        