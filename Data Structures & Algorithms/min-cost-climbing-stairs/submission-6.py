class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0]*(len(cost)+2)
        N = len(cost)
        for i in range(N-1,-1,-1):
            dp[i] = cost[i] + min(dp[i+1],dp[i+2])
        return min(dp[0],dp[1])

        # def dfs(i):
        #     if i in dp:
        #         return dp[i]
        #     if i>=N:
        #         return 0
        #     dp[i] = cost[i] + min(dfs(i+1),dfs(i+2))
        #     return dp[i]
        # return min(dfs(0),dfs(1))

        