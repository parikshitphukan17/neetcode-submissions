class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        N,M = len(s),len(t)
        dp = [0 for i in range(M+1)]
        dp[M] = 1
        for i in range(N-1,-1,-1):
            newDp = [0] *(M+1)
            newDp[M] = 1
            for j in range(M-1,-1,-1):
                newDp[j] = dp[j]
                if s[i] == t[j]:
                    newDp[j] += dp[j+1]
            dp = newDp
        return dp[0]

