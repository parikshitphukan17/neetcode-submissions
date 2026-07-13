class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        N = len(cost)
        dp = [0] * (N+1)
        for i in range(N-1,-1,-1):
            nxt = dp[i+1]
            if i<N-1:
                nxt = min(nxt,dp[i+2])
            dp[i] = cost[i] + nxt
        return min(dp[0],dp[1])
        # def climb(i):
        #     if i == N:
        #         return 0
        #     if i>N:
        #         return float("infinity")
        #     if i in dp:
        #         return dp[i]
        #     dp[i] = cost[i] + min(climb(i+1),climb(i+2))
        #     return dp[i]
        # return min(climb(0),dp[1])
        