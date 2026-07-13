class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        N,M = len(s),len(t)
        dp = [[0 for i in range(M+1)] for j in range(N+1)]
        for i in range(N+1):
            dp[i][M] = 1
        for i in range(N-1,-1,-1):
            for j in range(M-1,-1,-1):
                if s[i] == t[j]:
                    dp[i][j] = dp[i+1][j+1] + dp[i+1][j]
                else:
                    dp[i][j] = dp[i+1][j]
        return dp[0][0]

