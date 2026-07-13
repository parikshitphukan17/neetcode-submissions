class Solution:
    def climbStairs(self, n: int) -> int:
        dp = {}
        def dfs(cur):
            if cur in dp:
                return dp[cur]
            if cur == n:
                return 1
            if cur>n:
                return 0
            dp[cur] = dfs(cur+1) + dfs(cur+2)
            return dp[cur]
        return dfs(0)


        