class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        N = len(prices)
        dp = {}
        def dfs(buy,i):
            if i >= N:
                return 0
            if (buy,i) in dp:
                return dp[(buy,i)]
            if buy:
                dp[(buy,i)] = max(-prices[i] +dfs(False,i+1),dfs(buy,i+1))
            else:
                dp[(buy,i)] = max(prices[i] + dfs(True,i+2),dfs(buy,i+1))
            return dp[(buy,i)]
        return dfs(True,0)

            

            
        