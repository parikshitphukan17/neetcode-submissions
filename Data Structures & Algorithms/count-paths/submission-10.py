class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [0]*(n+1)
        dp[n-1] = 1
        for i in range(m-1,-1,-1):
            cur = [0]*(n+1)
            #cur[n-1] = 1 if i ==m-1 else 0
            for j in range(n-1,-1,-1):
                cur[j] += dp[j] + cur[j+1]
            dp = cur
        return dp[0]
        # def dfs(i,j):
        #     if i == m-1 and j == n-1:
        #         return 1
        #     if i == m or j == n:
        #         return 0
        #     if (i,j) in dp:
        #         return dp[(i,j)]
        #     dp[(i,j)] = dfs(i+1,j) + dfs(i,j+1)
        #     return dp[(i,j)]
        # return dfs(0,0)
        