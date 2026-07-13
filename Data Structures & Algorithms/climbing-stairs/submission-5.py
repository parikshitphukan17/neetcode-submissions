class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0]*(n+2)
        dp[n] = 1
        for i in range(n-1,-1,-1):
            dp[i] = dp[i+1]+dp[i+2]
        return dp[0]
        # def dfs(i):
        #     if i in dp:
        #         return dp[i]
        #     if i ==n:
        #         return 1
        #     if i>n:
        #         return 0
        #     dp[i] = dfs(i+1) + dfs(i+2)
        #     return dp[i]
        # return dfs(0)
        