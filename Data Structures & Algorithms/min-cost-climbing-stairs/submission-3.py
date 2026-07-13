class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = {}
        N = len(cost)
        def climb(i):
            if i == N:
                return 0
            if i>N:
                return float("infinity")
            if i in dp:
                return dp[i]
            dp[i] = cost[i] + min(climb(i+1),climb(i+2))
            return dp[i]
        return min(climb(0),dp[1])
        