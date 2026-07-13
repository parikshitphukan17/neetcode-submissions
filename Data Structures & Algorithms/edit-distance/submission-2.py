class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        N,M = len(word1),len(word2)
        dp = [j for j in range(M,-1,-1)]
        for i in range(N-1,-1,-1):
            newDp = [0]*(M+1)
            newDp[M] = N-i
            for j in range(M-1,-1,-1):
                if word1[i] == word2[j]:
                    newDp[j] = dp[j+1]
                else:
                    newDp[j] = 1+ min(newDp[j+1],dp[j],dp[j+1])
            dp = newDp
        return dp[0]
        