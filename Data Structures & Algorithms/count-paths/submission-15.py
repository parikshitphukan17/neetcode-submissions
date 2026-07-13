class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [0]*(n+1)
        dp[n-1] = 1
        for i in range(m-1,-1,-1):
            cur = [0]*(n+1)
            for j in range(n-1,-1,-1):
                cur[j] += dp[j] + cur[j+1]
            dp = cur
        return dp[0]

        
        