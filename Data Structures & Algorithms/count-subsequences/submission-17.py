class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        M,N = len(s),len(t)
        if N>M:
            return 0
        dp = [[0] * (N+1) for _ in range(M+1)]
        for i in range(M+1):
            dp[i][N] = 1

        for i in range(M-1,-1,-1):
            for j in range(N-1,-1,-1):
                dp[i][j] = dp[i+1][j]
                if s[i] == t[j]:
                    dp[i][j] += dp[i+1][j+1]
        return dp[0][0] 
        # def dfs(i,j):
        #     if j == N:
        #         return 1
        #     if i == M:
        #         return 0
        #     if (i,j) in dp:
        #         return dp[(i,j)]
        #     res = dfs(i+1,j)
        #     if s[i] == t[j]:
        #         res += dfs(i+1,j+1)
        #     dp[(i,j)] = res
        #     return dp[(i,j)]
        # return dfs(0,0)




      




        