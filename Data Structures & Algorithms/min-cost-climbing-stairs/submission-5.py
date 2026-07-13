class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = {}
        N = len(cost)
        def dfs(i):
            if i in dp:
                return dp[i]
            if i>=N:
                return 0
            dp[i] = cost[i] + min(dfs(i+1),dfs(i+2))
            return dp[i]
        return min(dfs(0),dfs(1))

        