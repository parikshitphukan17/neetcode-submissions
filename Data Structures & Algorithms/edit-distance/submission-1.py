class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        N,M = len(word1),len(word2)
        dp = [[0 for j in range(M+1)] for i in range(N)]
        dp.append([j for j in range(M,-1,-1)])
        for i in range(N):
            dp[i][M] = N-i
        
        for i in range(N-1,-1,-1):
            for j in range(M-1,-1,-1):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i+1][j+1]
                else:
                    dp[i][j] = 1+ min(dp[i][j+1],dp[i+1][j],dp[i+1][j+1])
        return dp[0][0]
        