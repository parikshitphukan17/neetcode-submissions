class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        def dfs(i):
            if i in dp:
                return dp[i]
            if i>=len(cost):
                return 0
            dp[i] = cost[i] + min(dfs(i+1),dfs(i+2))
            return dp[i]
        dp = {}
        res1 = dfs(0)
        dp = {}
        res2 = dfs(1)
        return min(res1,res2)
        

        