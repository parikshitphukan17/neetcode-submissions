class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        N,M = len(text1),len(text2)
        dp = [[0]*(M+1) for i in range(N+1)]
        for i in range(N-1,-1,-1):
            for j in range(M-1,-1,-1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i+1][j+1]
                else:
                    dp[i][j] = max(dp[i][j+1],dp[i+1][j])
        return dp[0][0]
        # def dfs(i,j):
        #     if i == N or j == M:
        #         return 0
        #     if (i,j) in dp:
        #         return dp[(i,j)]
        #     if text1[i] == text2[j]:
        #         dp[(i,j)] = 1 + dfs(i+1,j+1)
        #     else:
        #         dp[(i,j)] = max(dfs(i,j+1),dfs(i+1,j))
        #     return dp[(i,j)]
        # return dfs(0,0)

        


        # i i
        # c a t
        # j j j
        # c r a b t
        # if m :
        #     1 + dfs(i+1,j+1)
        # else:
        #     max(dfs(i+1,j),dfs(i,j+1))
        